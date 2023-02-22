import numpy as np

np.set_printoptions(precision=7, suppress=True, linewidth=100)


def neville_method(x_vals, y_vals, x):
    matrix = np.zeros((len(x_vals), len(x_vals)))

    for counter, row in enumerate(matrix):    #populate y values column
        row[0] = y_vals[counter]
    num_points = counter

    for i in range(1, len(x_vals)):
        for j in range(1, i+1):

            first_multiplication = (x - x_vals[i-1]) * matrix[i][j-1]
            second_multiplication = (x - x_vals[i]) * matrix[i-1][j-1]

            denominator = x_vals[i] - x_vals[i-1]

            coefficient = (first_multiplication - second_multiplication)/denominator
            matrix[i][j] = coefficient


    print(coefficient)

def newton_forward_coefficients(x_vals, y_vals):

    matrix = np.zeros((len(x_vals), len(x_vals)))

    for i, row in enumerate(matrix):
        row[0] = y_vals[i]

    for i in range(1, len(x_vals)):
        for j in range(1, i+1):
            #difference = [left - left-upper]/[span of x values]
            numerator = matrix[i][j-1] - matrix[i-1][j-1]
            denominator = x_vals[i] - x_vals[i-j]
            div_difference = numerator/denominator
            matrix[i][j] =  '{0:.7g}'.format(div_difference)

    coeffs = []
    for i in range(1, len(x_vals)):
        coeffs.append(matrix[i][i])
    print(coeffs)

    return coeffs

def newton_approx_value(coeffs, x_vals, y_vals, x):
    recurring_x_span = 1
    recurring_px = y_vals[0]

    for index, coefficient in enumerate(coeffs):
        recurring_x_span *= x - x_vals[index]
        recurring_px += coefficient * recurring_x_span

    print(recurring_px)

def hermite_interpolation(x_vals, y_vals, slopes):
    num_points = len(x_vals)
    matrix = np.zeros((2*num_points, 2*num_points))

    k = 0
    for i in range(0, 2*num_points, 2):
        matrix[i][0] = x_vals[k]
        matrix[i+1][0] = x_vals[k]

        matrix[i][1] = y_vals[k]
        matrix[i+1][1] = y_vals[k]

        matrix[i+1][2] = slopes[k]
        k+=1

    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            #skip prefilled values:
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            # numerator = left - diagonal left
            numerator: float = matrix[i][j-1] - matrix[i-1][j-1]
            # denominator = current x - starting x
            denominator = matrix[i][0] - matrix[i-j+1][0]
            
            operation = numerator/denominator
            matrix[i][j] = operation

    print(matrix)


# 1. Using Neville’s method, find the 2nd degree interpolating value for f(3.7) for the following set of data
    #x = [3.6, 3.8, 3.9]
    #f(x) = [1.675, 1.436, 1.318]

given_x = [3.6, 3.8, 3.9]
given_y = [1.675, 1.436, 1.318]
approx = 3.7
neville_method(given_x, given_y, approx)


# 2. Using Newton’s forward method, print out the polynomial approximations for degrees 1, 2, and 3 using the following set of data
x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]

coefficients = newton_forward_coefficients(x, y)

# 3. Using the results from 3, approximate f(7.3)
approx = 7.3
newton_approx_value(coefficients, x, y, approx)

# 4. Using the divided difference method, print out the Hermite polynomial approximation matrix
    #3.6 1.675 -1.195
    #3.8 1.436 -1.188
    #3.9 1.318 -1.182
x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]
y_prime = [-1.195, -1.188, -1.182]

hermite_interpolation(x, y, y_prime)