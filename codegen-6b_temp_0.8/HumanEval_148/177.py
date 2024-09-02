
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    def bf_inner(curr, arr, count, res):
        for i in range(count):
            if arr[i] == curr:
                res.append(arr[i+1])
                return res
        return res
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()
    res = []
    planet1_pos = PLANETS.index(planet1)
    planet2_pos = PLANETS.index(planet2)
    curr = planet1_pos
    if planet1_pos < planet2_pos:
        arr = PLANETS[planet1_pos:planet2_pos+1]
    else:
        arr = PLANETS[planet1_pos:planet2_pos-1:-1]
    count = len(arr)
    if planet1_pos == planet2_pos:
        res.append(arr[0])
        return tuple(res)
    while count > 0:
        res = bf_inner(curr, arr, count, res)
        curr += 1
        if curr == count:
            break
        count -= 1
    return tuple(res)    
