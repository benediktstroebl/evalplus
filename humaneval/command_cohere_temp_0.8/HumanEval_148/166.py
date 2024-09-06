```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = i + 1
        if planets[i] == planet2:
            p2 = i + 1
            fl = True    
    if not fl:
        return ()
    if p2 < p1:
        temp = p2
        p2 = p1
        p1 = temp
    res = []
    if p1 > 0:
        res.append(planets[p1 - 1])
    if p2 < 7:
        res.append(planets[p2 + 1])
    return tuple(res)
```

The function `bf` takes in two parameters `planet1` and `planet2` and returns a tuple containing all the planets between the two planets in terms of proximity to the sun. The function first checks if the inputted parameters are valid planet names and then returns an empty tuple if they are not. The function uses a list called `planets` to store all the planets in the solar system to easily iterate through each planet's index number. It then uses variables `p1` and `p2` to store the index numbers of the inputted planets. After checking if the inputted planets are valid, it checks if `p2` is after `p1` in the solar system and swaps the variables if they are not. The function then adds the planets to the tuple in the order they come in the solar system, using conditional statements to add them to the tuple accordingly. It then returns the tuple.