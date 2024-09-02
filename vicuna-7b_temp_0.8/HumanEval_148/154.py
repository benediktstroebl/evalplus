
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    elif planet1 == "Jupiter" or planet2 == "Jupiter":
        # Jupiter is always last
        return (planet1,) + (planet2,)
    elif planet1 < planet2:
        # Get the planets in the correct order
        planets = (planet1, planet2)
        if planet1 == "Mercury":
            planets = (planet2, planet1)
        if planet2 == "Mercury":
            planets = (planet1, planet2)
        if not isinstance(planets, tuple) or not len(planets) > 2:
            return ()
        return tuple(sorted(planets, key=lambda x: (x.distance_to_planet(planet2), x.distance_to_planet(planet1))) )
    elif planet2 < planet1:
        planets = (planet1, planet2)
        if planet1 == "Mercury":
            planets = (planet2, planet1)
        if planet2 == "Mercury":
            planets = (planet1, planet2)
        if not isinstance(planets, tuple) or not len(planets) > 2:
            return ()
        return tuple(sorted(planets, key=lambda x: (x.distance_to_planet(planet2), x.distance_to_planet(planet1))) )
    else:
        return ()