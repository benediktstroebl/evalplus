```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It takes advantage of the fact that the greatest common divisor will remain unchanged if either variable is replaced with the remainder of their division. 

It's an efficient approach that solves the problem by making a finite number of iterations. The time complexity of each iteration is `O(Log(MIN(a,b)))`, and the number of iterations is controlled by the value of the lesser of the two inputs. Thus, the overall time complexity of the algorithm is `O(Log(MIN(a,b)))`. 

The algorithm terminates when `b` is reduced to zero. At this point, the value of `a` is the GCD of the initial inputs. The output is then returned from the recursive call stack. 

Let's demonstrate it with an example using the initial values provided in the problem statement:
```python
greatest_common_divisor(25, 15)
```
The execution will proceed as follows:
- `greatest_common_divisor(25, 15)` - The lesser of `25` and `15` is `15`. Thus, the algorithm will proceed with `b%a`, which is `15%25` which is `15`
- `greatest_common_divisor(15, 25)` - The lesser of `15` and `25` is `15`. So, the algorithm proceeds with `b%a`, which is `15%25` (again) which is `15`
- `greatest_common_divisor(15, 15)` - The lesser of `15` and `15` is `15`. So, the algorithm proceeds with `b%a`, which is `15%15` which is `0`
- `greatest_common_divisor(0, 15)` - Now, the algorithm proceeds with `b%a`, which is `0%15` which is `0`
- The termination condition is met because `b` (15) was reduced to zero. The value of `a` (`0`) is the GCD of the original inputs (`25` and `15`)
- The output is `0`, which is the greatest common divisor of `25` and `15`

This algorithm is efficient for finding the GCD of two integers. It showcases the benefits of the Euclidean algorithm and demonstrates how recursion can be used to solve mathematical problems.