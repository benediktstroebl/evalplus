
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
    # Please print out which test cases are FAILED and WHY.
    # Do NOT leave a "TODO" line in the code when you are asked to do so.

    planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()
    planet_indexes = {planet:i for i, planet in enumerate(planets)}

    if planet1 not in planet_indexes or planet2 not in planet_indexes:
        return ()

    lower_index = min(planet_indexes[planet1], planet_indexes[planet2])
    higher_index = max(planet_indexes[planet1], planet_indexes[planet2])

    return tuple(planets[i] for i in range(lower_index, higher_index+1) if i != planet_indexes[planet1] and i != planet_indexes[planet2])

