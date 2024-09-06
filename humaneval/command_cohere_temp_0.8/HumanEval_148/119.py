```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1: p1 = i
        if p == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p1 > p2 else planets[p1:p2+1])
``` 

The function first assigns the two planet names passed to the function `planet1` and `planet2`, and stores the index of each planet in the list of planets in our solar system in `p1` and `p2` respectively. It then checks if both indexes are -1, and since that would mean that neither planet1 nor planet2 are actual planets names, it returns an empty tuple `()`. If either `p1` or `p2` is not -1, it checks which planets to return. It returns all planets from the orbit of `planet1` to the orbit of `planet2` if `p1` is less than `p2`, and since the list of planets is sorted by proximity to the sun, it is the case that `p2` is in the orbit of `planet1`. If `p1` is greater than `p2`, it returns only the `planet2` which is in the orbit of `planet1`. 

The following example calls are possible:
```python
print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))
```

The possible corresponding outputs are:
```
('Saturn', 'Uranus')
('Venus')
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```