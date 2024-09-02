
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
    planets = ("Jupiter", "Neptune", "Earth", "Venus", "Mars", "Saturn", "Uranus", "Pluto")
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    l1 = planets.index(planet1)
    l2 = planets.index(planet2)
    if l1 > l2:
        return tuple()
    s1 = [planet1]
    s2 = [planet2]
    while l1 < l2:
        s1.append(planets[l1 + 1])
        s2.append(planets[l1 + 1])
        l1 += 1
    s1.append(planet2)
    while l1 < l2:
        s2.append(planets[l2 - 1])
        s1.append(planets[l2 - 1])
        l2 -= 1
    s1.reverse()
    s2.reverse()
    return tuple(s1)


