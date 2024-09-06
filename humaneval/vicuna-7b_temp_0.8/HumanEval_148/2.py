
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
    if not planet1 or not planet2:
        return ()

    if planet1.lower() < planet2.lower():
        return ()

    if planet2.lower() < planet1.lower():
        return ()

    if not isinstance(planet1, basestring) or not isinstance(planet2, basestring):
        return ()

    planets = []
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        if planet.lower() < planet1.lower():
            if planet.lower() < planet2.lower():
                if isinstance(planet, basestring):
                    planets.append(planet)

    if isinstance(planet1, basestring):
        for planet in planets:
            if planet.lower() > planet1.lower():
                if isinstance(planet, basestring):
                    planets.append(planet)
    else:
        for planet in planets:
            if planet.lower() < planet1.lower():
                if isinstance(planet, basestring):
                    planets.append(planet)

    if isinstance(planet2, basestring):
        for planet in planets:
            if planet.lower() > planet2.lower():
                if isinstance(planet, basestring):
                    planets.append(planet)
    else:
        for planet in planets:
            if planet.lower() < planet2.lower():
                if isinstance(planet, basestring):
                    planets.append(planet)

    return sorted(planets, key=lambda x: x.lower() - planet1.lower())

example1 = bf("Jupiter", "Neptune")
