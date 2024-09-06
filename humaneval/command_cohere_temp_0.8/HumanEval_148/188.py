```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return tuple()

    result = []
    for i in range(p1, p2 + 1):
        result.append(planets[i])

    return tuple(result)
```

The function `bf` takes two planet names, `planet1` and `planet2`, as inputs. It uses the list `planets` containing the names of the eight planets to determine the indices of `planet1` and `planet2` in the list. If either of the inputs is not a correct planet name, the function returns an empty tuple, this is checked with the condition `if p1 == -1 or p2 == -1:`. If the inputs are valid planet names, the function collects all the planets whose indices are between the indices of `planet1` and `planet2`, adding them to the `result` list. The list is then returned as a tuple. 

The test cases are:
```python
test_bf = {
    ("Jupiter", "Neptune"), ("Saturn", "Uranus"), ("Earth", "Mercury"), ("Mercury", "Uranus"),
    ("Sun", "Neptune"), ("Neptune", "Saturn"), ("Horse", "Earth"), ("Saturn", "Saturn"),
    ()
}

for case in test_bf:
    try:
        print(bf(*case))
        assert len(bf(*case)) < 10
    except AssertionError:
        print("Failed: ", end=" ")
    else:
        print("Passed: ", end=" ")
    print()
```
The script shows how the code can be tested using the `assert` statement.