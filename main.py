import LinearApproximation as la
import sympy as sp


def diff(function):
    x, y = sp.symbols('x y')
    return str(sp.diff(function, x))


if __name__ == "__main__":
    function = input("Input a function = ")
    derivative_function = diff(function)
    print("The derivative of this function = " + derivative_function)

    function = function.replace('x', 'np.array({})')
    derivative_function = derivative_function.replace('x', 'np.array({})')

    border_range = [int(i) for i in input("Enter the borders separated by a space = ").strip().split()]
    intervals = int(input("Enter the number of approximation nodes = "))

    approximation = la.LinearApproximation(function, derivative_function, border_range, intervals)
    approximation.set_ranges()
    approximation.approximate_graph()
