```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange:
        return "YES"
    else:
        return "NO"
```

The function **exchange** takes two lists, **lst1** and **lst2**, as input and returns a string indicating whether it is possible to exchange elements between the two lists to make **lst1** a list of only even numbers. The function checks if there is at least one even number in **lst1** by iterating over the list and checking if each element is an integer and if it's divisible by 2 without any remainder. If there is at least one even number in **lst1**, it returns **"YES"** since it's possible to exchange elements with even numbers only from **lst2** to make the list consist of even numbers only. If there are no even numbers in **lst1**, it returns **"NO"**.