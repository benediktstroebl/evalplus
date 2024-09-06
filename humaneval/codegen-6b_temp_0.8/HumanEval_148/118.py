
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
    # description of what we need:
    # make a dictionary (key = planet name)
    # for each key, find the orbits between the 2 planets
    # then sort the orbits by proximity to the sun.
    # return a tuple of the planets that close with the sun

    d = {}
    for p in planetNames:
        d[p] = findOrbits(p, planetNames, len(orbitMap))

    # get solutions
    answer = []
    for planet1 in d.keys():
        orbit1 = d[planet1]
        for planet2 in d.keys():
            orbit2 = d[planet2]
            if planet1 != planet2:
                if orbit1 and orbit2:
                    if orbit1[-1] < orbit2[0]:
                        if (orbit2[0] - planet1 in orbit1) or (planet1 - orbit2[-1] in orbit2):
                            answer.append((planet1, planet2))
    # order the answers by the distance from the sun
    answer = sorted(answer, key=lambda x: abs(sun - x[1]) + abs(sun - x[0]))
    return tuple(answer)
