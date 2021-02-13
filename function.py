# import modules
import numpy as np
import matplotlib.pyplot as plt

# our function
def func(x) -> float:
    return np.tan(x)/x

def build_plot():
    # input begin and end of our plot
    begin = - np.pi
    end =  np.pi
    # input step
    step = 0.1


    # calculate drawing quality
    drawing_quality = int((end - begin) / step)

    # create a drawing with a coordinate plane
    plt.subplots()
    # create an area in which there will be - the graph is displayed
    # x values to be displayed
    # number of elements in the created array
    # graph drawing quality
    x = np.linspace(begin, end, drawing_quality)
    # draw a graph
    plt.plot(x, func(x))
    # showing the schedule
    plt.show()

    # output our table of results
    while begin < end:
        print('x =', begin, '\t| y =', func(begin))
        begin += step

if __name__ == '__main__':
    build_plot()


