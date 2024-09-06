def concatenate(*args):
    strings = ["{}".format(str) for str in args]
    return "".join(strings) if strings else "''"