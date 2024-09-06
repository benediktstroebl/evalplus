Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate = n
    if ate + need > rem:
        ate = rem
    print(f"Rabbit eats {ate} carrots, it remains with {rem-ate} carrots.")
    return [n+ate, rem-ate]
```

The function prints the scenario about how many carrots the rabbit eats and then returns the expected output, which is a list of two items: the total number of carrots eaten after the meal and the number of carrots left after the meal. 

This approach will work successfully if the amount of carrots needed to eat is less than or equal to the remaining stock. Otherwise, the rabbit will eat the entire remaining stock of carrots, but will still be hungry (printable message included) despite returning an answer. 

As per the constrained values, it assumes that the variables are integers and their values are within the range of 0 to 1000. 

This is a self-contained Python script that solves the given problem in a markdown code block. Let me know if any clarification is needed.