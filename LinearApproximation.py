import numpy as np
import matplotlib.pyplot as plt


class LinearApproximation:
    def __init__(self, original_function, derivative_function, border_range, intervals):
        self.original_function = original_function
        self.derivative_function = derivative_function
        self.border_range = border_range
        self.intervals = intervals

    def set_ranges(self):
        self.spot_points = np.linspace(self.border_range[0], self.border_range[1], self.intervals)
        del_x = (self.border_range[1] - self.border_range[0]) / ((self.intervals - 1) * 2)
        self.slopes = eval(self.derivative_function.format(list(self.spot_points)))
        self.value_ranges = list(zip(self.spot_points - del_x, self.spot_points + del_x))

    def approximate_graph(self):
        for i, j in enumerate(self.value_ranges):
            x_t = np.linspace(j[0], j[1], 2)
            y_t = self.slopes[i] * (x_t - self.spot_points[i]) + eval(
                self.original_function.format(self.spot_points[i]))
            if i == 0:
                plt.plot(x_t, y_t, color='green', label='Approximable function')
            else:
                plt.plot(x_t, y_t, color='green')
        plt.plot(
            np.linspace(self.border_range[0], self.border_range[1], 100),
            eval(self.original_function.format(list(np.linspace(self.border_range[0], self.border_range[1], 100)))),
            color='blue',
            label='Base function'
        )
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
