```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            res.append(f"{roman_digit(i)}{mini_roman(n-i)}")
            n = n - i
    if n > 0:
        res.append(f"{roman_digit(n)}{mini_roman(0)}")
    return "".join(res)

def roman_digit(n):
    if n == 1:
        return "i"
    elif n == 5:
        return "v"
    elif n == 10:
        return "x"
    elif n == 50:
        return "l"
    elif n == 100:
        return "c"
    elif n == 500:
        return "d"
    elif n == 1000:
        return "m"

def mini_roman(n):
    if n == 0:
        return ""
    elif n == 1:
        return "i"
    elif n == 2:
        return "ii"
    elif n == 3:
        return "iii"
    elif n == 4:
        return "iv"
    elif n == 6:
        return "vi"
    elif n == 7:
        return "vii"
    elif n == 8:
        return "viii"
    elif n == 9:
        return "ix"
    elif n == 10:
        return "x"
    elif n == 11:
        return "xi"
    elif n == 20:
        return "xx"
    elif n == 30:
        return "xxx"
    elif n == 40:
        return "xl"
    elif n == 50:
        return "l"
    elif n == 60:
        return "lx"
    elif n == 70:
        return "lxx"
    elif n == 80:
        return "lxxx"
    elif n == 90:
        return "xc"
    elif n == 99:
        return "xcix"
    elif n == 100:
        return "c"
    elif n == 101:
        return "ci"
    elif n == 102:
        return "cii"
    elif n == 103:
        return "ciii"
    elif n == 104:
        return "civ"
    elif n == 105:
        return "cv"
    elif n == 110:
        return "cx"
    elif n == 111:
        return "cxli"
    elif n == 120:
        return "cxx"
    elif n == 121:
        return "cxxi"
    elif n == 130:
        return "cxxiii"
    elif n == 140:
        return "cl"
    elif n == 141:
        return "cli"
    elif n == 150:
        return "clii"
    elif n == 160:
        return "clix"
    elif n == 161:
        return "clxi"
    elif n == 170:
        return "clxx"
    elif n == 180:
        return "clxxx"
    elif n == 190:
        return "cd"
    elif n == 191:
        return "cdi"
    elif n == 192:
        return "cdii"
    elif n == 193:
        return "cdiii"
    elif n == 194:
        return "cdiv"
    elif n == 195:
        return "cdv"
    elif n == 200:
        return "dc"
    elif n == 201:
        return "dci"
    elif n == 202:
        return "dcii"
    elif n == 203:
        return "dciii"