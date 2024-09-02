
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
    # coding: utf-8
    # Alphabetical order
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_order.reverse()
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    if planet1 in planet_order and planet2 in planet_order:
        return tuple(planet_order[planet_order.index(planet1) : planet_order.index(planet2) + 1])
    # Reversed order
    else:
        planet_order.reverse()
        return tuple(planet_order[planet_order.index(planet1) : planet_order.index(planet2) + 1])
