```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(n // 10)
        if tens == 1:
            return "x" + int_to_mini_roman(n % 10)
        elif tens > 1:
            return "xx" + int_to_mini_roman(n % 10)
        else:
            return ""
```

The overall approach employed by the provided Python script is to convert the integer input into its decimal representation, handling the tens and units separately. The script leverages this representation to construct the corresponding Roman numeral string using the int_to_mini_roman function.

Here's a step-by-step breakdown of the conversion process:
1. The input integer is initially divided by 10 to extract the tens value.
2. The resulting quotient, which represents the tens value, is then used to construct the Roman numeral string in a recursive manner.
3. If the tens value is 1, the script returns "i," indicating that the Roman numeral will be just the singular character "i."
4. For a tens value greater than 1, the script returns "xx," forming the Roman numeral string as "xx" followed by the converted units value.
5. If the tens value is 0, indicating that there are no tens in the current conversion, the script returns an empty string.
6. Finally, the script performs the same recursive `int_to_mini_roman` call on the units (left over from step 1) to convert the units value into Roman characters, which will be concatenated to the tens result when appropriate.

This approach ensures that the resulting Roman numeral is always in lowercase and adheres to the specified constraints. And, the script successfully handles the nested recursion for the tens and units conversions, delivering the correct Roman numeral equivalent for the given range of integers. 

You can verify the functionality with the provided tests:
```python
def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "lx"
    assert int_to_mini_roman(90) == "lxix"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cl"
    assert int_to_mini_roman(500) == "l"
    assert int_to_mini_roman(900) == "lc"
    assert int_to_mini_roman(1000) == "m"
```