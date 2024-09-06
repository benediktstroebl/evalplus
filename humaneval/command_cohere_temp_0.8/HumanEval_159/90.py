Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```

This function takes in three variables: `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten, and `rem` which is the number of remaining carrots. The function returns a list containing two integers: the number of carrots eaten after the meal and the number of carrots remaining after the rabbit's meal. 

The function includes a constraint that if there aren't enough carrots to fulfill the 'need', the rabbit will eat all the remaining carrots, however, it will still be hungry and put effort into finding more carrots to eat. As the script fits the prompt's guidelines, the function should run and produce correct outputs for the provided test examples. 

Let's test it out:
```python
print(eat(5, 6, 10))
print(eat(4, 8, 9))
print(eat(1, 10, 10))
print(eat(2, 11, 5))
```

Here are the outputs:
```
[11, 4]
[12, 1]
[11, 0]
[7, 0]
```
All examples align with the expected outputs as illustrated in the original prompt.