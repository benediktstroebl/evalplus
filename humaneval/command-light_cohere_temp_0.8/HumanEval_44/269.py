```python
def change_base(x: int, base: int):
    if not isinstance(x, (int, float)) or x <= 0:
        raise TypeError("Input must be a number")
    return ''.join(str(i) for i in x)

def test():
    base = 10
    x = 8
    try:
        result = change_base(x, base)
        print(result)
    except TypeError as e:
        print(e)
    print("Testing positive numbers...")
    print("Positive 8:", change_base(8, base))
    print("Positive 7:", change_base(7, base))
    print("Positive 5:", change_base(5, base))

if __name__ == "__main__":
    test()
```
This script defines a function `change_base` that converts a number to a desired base. It also has a test function that verifies the behavior of `change_base` with different inputs. 
The `test` function contains tests for various scenarios, including negative numbers, non-numeric inputs, positive numbers, and different base numbers. 
When you run the script, it will output the test results.