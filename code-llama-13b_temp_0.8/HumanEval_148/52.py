
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
    planets = [('Mercury', 57909227), ('Venus', 108208003), ('Earth', 149600000),
               ('Mars', 227943829), ('Jupiter', 778368799), ('Saturn', 1429461509),
               ('Uranus', 2870995458), ('Neptune', 449825628)]
    res = []
    for planet, dist in planets:
        if planet in [planet1, planet2]:
            res.append(planet)
    if len(res) == 2:
        if res[0] == planet1:
            planet1 = res[1]
            planet2 = res[0]
        else:
            planet1 = res[0]
            planet2 = res[1]
        res = []
    if not planet1 in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    if not planet2 in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    for planet, dist in planets:
        if planet != planet1 and planet != planet2:
            if dist < planets[planets.index((planet1, 0))][1] and dist > planets[planets.index((planet2, 0))][1]:
                res.append(planet)
    return tuple(sorted(res))
