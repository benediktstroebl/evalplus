
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
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        # Only return planets that orbit further away from the sun than Jupiter
        # (ignoring the fact that this is not correct astronomy)
        return (planet2,) + sorted(range(8))[1:-1]
    elif planet1 == "Mercury" or planet2 == "Mercury":
        # Only return planets that orbit closer to the sun than Mercury
        # (ignoring the fact that this is not correct astronomy)
        return (planet1,) + sorted(range(8))[:1]
    elif planet2 == "Saturn" or planet1 == "Saturn":
        # Only return planets that orbit further away from the sun than Saturn
        # (ignoring the fact that this is not correct astronomy)
        return (planet1,) + sorted(range(8))[1:-1]
    elif planet1 == "Saturn" or planet2 == "Saturn":
        # Only return planets that orbit closer to the sun than Saturn
        # (ignoring the fact that this is not correct astronomy)
        return (planet2,) + sorted(range(8))[:1]
    elif planet2 == "Uranus" or planet1 == "Uranus":
        # Only return planets that orbit further away from the sun than Uranus
        # (ignoring the fact that this is not correct astronomy)
        return (planet1,) + sorted(range(8))[1:-1]
    elif planet1 == "Uranus" or planet2 == "Uranus":
        # Only return planets that orbit closer to the sun than Uranus
        # (ignoring the fact that this is not correct astronomy)
        return (planet2,) + sorted(range(8))[:1]
    elif planet2 == "Neptune" or planet1 == "Neptune":
        # Only return planets that orbit further away from the sun than Neptune
        # (ignoring the fact that this is not correct astronomy)
        return (planet1,) + sorted(range(8))[1:-1]
