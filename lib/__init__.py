import numpy as np
import matplotlib.pyplot as plt

def find_nearest_index(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def get_offset_x(shifted, reference, plot=False):

    # originally from Matlab source: 
    #
    # function [ xoffset, yoffset ] = getOffset( moving, fixed )
    # [ypeak, xpeak] = find(c == max(c(:)));
    # [ysize,xsize] = size(moving);
    # yoffset = ypeak - ysize;
    # xoffset = xpeak - xsize;

    norm_reference = np.linalg.norm(reference)
    _reference = reference/norm_reference

    norm_shifted = np.linalg.norm(shifted)
    _shifted = shifted/norm_shifted

    c = np.correlate(_shifted, _reference,'full')

    if plot==True:
        plt.rcParams['figure.figsize'] = FigureSize.NARROW
        fig, axes = plt.subplots()
        plt.plot(c)
        plt.show()

    return np.argmax(c)-len(shifted)

class FigureSize():
    THIN     = [24, 3]
    NARROW   = [24, 8]
    MEDIUM   = [24, 15]
    LARGE    = [24, 24]

