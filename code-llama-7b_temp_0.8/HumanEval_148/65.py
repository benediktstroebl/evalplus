
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
    # planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # orders = {"Mercury" : 1, "Venus" : 2, "Earth" : 3, "Mars" : 4, "Jupiter" : 5, "Saturn" : 6, "Uranus" : 7, "Neptune" : 8}
    # planet1_order = orders[planet1]
    # planet2_order = orders[planet2]
    # if planet1_order < planet2_order:
    #     return tuple([planet for planet in planets[planet1_order:planet2_order+1]])
    # elif planet1_order > planet2_order:
    #     return tuple([planet for planet in planets[planet2_order+1:planet1_order+1]])
    # else:
    #     return ()

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    orders = {"Mercury" : 1, "Venus" : 2, "Earth" : 3, "Mars" : 4, "Jupiter" : 5, "Saturn" : 6, "Uranus" : 7, "Neptune" : 8}
    planet1_order = orders[planet1]
    planet2_order = orders[planet2]
    if planet1_order < planet2_order:
        return tuple(planets[planet1_order+1:planet2_order])
    elif planet1_order > planet2_order:
        return tuple(planets[planet2_order+1:planet1_order])
    else:
        return ()

    # alternatively
    # return tuple(planets[orders[planet1]+1:orders[planet2]])

    # planets = ("Mercury", "Venus
