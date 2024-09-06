import numpy as np
def iscube(a):
    result = np.ceil(a ** (1/3))
    return result == int(result)