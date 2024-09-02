
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
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth":
        pl1 = planet1
    elif planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn":
        pl1 = planet2
    elif planet1 == "Uranus" or planet1 == "Neptune":
        pl1 = planet1
    elif planet1 == "Pluto" or planet1 == "Sun":
        pl1 = planet1
    else:
        return tuple()
    if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth":
        pl2 = planet2
    elif planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn":
        pl2 = planet2
    elif planet2 == "Uranus" or planet2 == "Neptune":
        pl2 = planet2
    elif planet2 == "Pluto" or planet2 == "Sun":
        pl2 = planet2
    else:
        return tuple()

    if pl1 == "Sun" and pl2 == "Sun":
        return tuple()
    if pl1 == "Sun" or pl2 == "Sun":
        return ("Sun",)

    xp1 = str(bin(planets.index(pl1))).split('b')[1]
    xp2 = str(bin(planets.index(pl2))).split('b')[1]
    if xp1 == xp2:
        return tuple()
    xp1 = "0"*(8-len(xp1)) + xp1
    xp2 = "0"*(8-len(xp2)) + xp2

    for i in range(1,len(xp1)):
        if xp1[-i:][::-1] != xp2[-i:][::-1]:
            return tuple(planets[j] for j in range(len(planets)-i,len(planets)))
    return tuple(planets[j] for j in range(len(planets)-i,len(planets)))
