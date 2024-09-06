```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Returing boolueana availible since Python 3.5, propose user to upgrate
    return a ** 3 == int(a ** 3)
```

To get the above result, a number of forms and algorithms were taken into account. The basic procedure is as follows:
1. If the number is 0, it is a cube since any number multiplied by itself three times equals 0. Therefore, iscube(0) = True.
2. We square the number a twice and then compare the result with a:
    - iscube(1) = True, because a ** 3 = a ** 2 * a = 1 * a * a = a ** 2 * a, and 1 * a * a is equal to a ** 2 * a when a is an integer.
    - iscube(4) = False, because 4 ** 3 = 64, and 64 != 4 * 4 * 4.
3. The following cases can be reasoned similarly:
    - iscube(-1) = True, because (-1) ** 3 = -1 * -1 * -1 = -1 * 1 * -1 = -1 ** 2 * -1
    - iscube(2) = False, because 2 ** 3 = 8, and 8 != 2 * 2 * 2.
4. These cases require more careful examination due to the possibility of simplification:
    - iscube(8) = True, because 8 ** 3 = 8 * 8 * 8 = 512, and 512 can be simplified to 4 * 2 * 2 * 2 * 2 * 2 * 2 * 2, which proves it is a cube.
    - iscube(27) = True, because 27 ** 3 = 27 * 27 * 27 = 19,683, which can be simplified to 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3, proving it is a cube.
    - iscube(64) = True, because 64 ** 3 = 64 * 64 * 64 = 262,144, which can be simplified to 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4, proving it is a cube.
5. The following cases can be handled similarly to those presented in point 2:
    - iscube(180) = False, because 180 ** 3 = 2,592,000, and 22592000 != 2 * 2 * 2 * 2 * 2 * 2 * 2 * 3 * 3 * 3 * 3 * 3
    - iscube(125) = True, because 125 ** 3 = 125 * 125 * 125 = 28,125,625, which can be simplified to 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5, proving it is a cube. 

This problem can be solved in various ways, but the most effective method involves checking if the number is equal to its cube root cube after calculating its cube.