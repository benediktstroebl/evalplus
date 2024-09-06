```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the given base.

    :type x : int,
    :type base : int
    :rtype string
    """
    if x < 0 or base < 0 or base < 2 or x < base:
        raise ValueError("Invalid input values")
    result = []
    while x > 0:
        digit = x % base
        result.append(str[format(digit))
        x //= base
    return "".join(result)

# Unit tests
test_change_base = []
test_change_base.push((8 string(change_base(-3, 10)))
test_change_base.push("22")
test_change_base.push("81")
test_change_base.push("10^3")
test_change_base.push("111")
test_change_base.push("10^101")
test_change_base.push(change_base(-3, 2))
test_change_base.push("1000")
test_change_base.push("111")
test_change_base.push(change_base(8, 101))
test_change_base.push("22")
test_change_base.push("81")
test_change_base.push("1000^11")
test_change_base.push("111^2")

def main():
    assert test_change_base == [
        "22",
        "22",
        "22",
        "22",
        "22",
        "1000",
        "111",
        "111",
        "111",
        "111",
        "22",
        "22",
        "22",
        "22",
    ]

if __name__ == "__main__":
    main()
```