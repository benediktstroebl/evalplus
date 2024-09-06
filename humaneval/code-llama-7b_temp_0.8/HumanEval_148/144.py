
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
    # create planets and their distances
    planets = {"Mercury":1, "Venus":2, "Earth":3, "Mars":4, "Jupiter":5, 
        "Saturn":6, "Uranus":7, "Neptune":8}

    planets_order = []
    for planet in planets:
        # add planets in order of distance
        if (planets[planet] > planets[planet1]) and (planets[planet] < planets[planet2]):
            planets_order.append(planet)

    # return planets between distance of planet1 and planet2
    if planets_order:
        return tuple(planets_order)
    else:
        return ()
