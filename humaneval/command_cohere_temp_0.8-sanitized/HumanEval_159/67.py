def eat(n, need, rem):
    var = n + need
    if var > rem:
        var = rem
    print(f'rabit eating {var} carrots, remaining {rem-var}')
    return [n+need, rem-var]