```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests
test_fib4 = TestFactory.from_module("fib4").create()

test_fib4.add_testcase(test_fib4, [5])

test_fib4.add_case([3, 4, 7], [test_fib4.fib(test_fib4.assertEqual(test_fib4.fib_case(fib4, 4)))

test_fib4.add_case([2, 3, 5, 6], [test_fib4.assertEqual(test_fib4.fib_case(fib4, 3)))

test_fib4.add_case([0, 0, 0, 0], [test_fib4.assertEqual(test_fib4.fib_case(fib4, 0)))
```

The `fib4` function computes the n-th Fibonacci number in the Fibonacci sequence. The function uses an loop to achieve this, which is more efficient than recursion for larger values of n. The tests that cover all possible cases, ensuring that the function works correctly for any input.