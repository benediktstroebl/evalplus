
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

    p1_orbit = planet_orbit(planet1)
    p2_orbit = planet_orbit(planet2)
    if p1_orbit == 0 or p2_orbit == 0:
        return ()
    i = 0
    j = 0
    res = ()
    while i < len(p1_orbit) and j < len(p2_orbit):
        if p1_orbit[i] < p2_orbit[j]:
            res += (p1_orbit[i],)
            i += 1
        elif p1_orbit[i] > p2_orbit[j]:
            res += (p2_orbit[j],)
            j += 1
        else:
            res += (p1_orbit[i],)
            i += 1
            j += 1
    while i < len(p1_orbit):
        res += (p1_orbit[i],)
        i += 1
    while j < len(p2_orbit):
        res += (p2_orbit[j],)
        j += 1
    return res
