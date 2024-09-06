Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate, leftovers = 0, 0
    while need > 0 and rem > 0:
        ate += min(need, rem)
        need -= ate
        rem -= 1
        leftovers += ate
    return [n + ate, leftovers]
```

This function uses a while loop that continues until either `need` or `rem` reaches zero. Each iteration calculates the minimum between `need` and `rem` and adds that value to the `ate` counter. Then it subtracts the eaten amount from both `need` and `rem`, and adds that eaten amount to the `leftovers` counter. Finally, the function returns a list containing the final values of `ate` and `leftovers`.

Here's the commented code explaining the above algorithm:
```python
# Initialize two variables to track the total number of carrots eaten and the remaining number of carrots
ate, leftovers = 0, 0

# Start the loop where the rabbit eats carrots
while need > 0 and rem > 0:
    # Min function is used to find the minimum number of carrots that the rabbit can eat from the remaining stock
    # This loop will eat as many carrots as possible to reach the desired amount of eating
    ate += min(need, rem)

    # Subtract the amount eaten from the need and remaining counters
    need -= ate
    rem -= 1

    # Add the amount eaten to the leftovers counter
    leftovers += ate

# Return a list containing the total number of carrots eaten and the number of carrots left after eating
return [n + ate, leftovers]
```