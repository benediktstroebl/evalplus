
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
    planets = {
        "Mercury": 0.387,
        "Venus": 0.723,
        "Earth": 1,
        "Mars": 1.524,
        "Jupiter": 5.203,
        "Saturn": 9.539,
        "Uranus": 19.181,
        "Neptune": 30.061
    }

    try:
        start_d = planets[planet1]
        end_d = planets[planet2]

        if start_d > end_d:
            # Swap the two
            start_d, end_d = end_d, start_d
        # Now we know that start_d is smaller than end_d

        # Get a list of all of the planets and their distances
        planet_d = [(name, dist) for name, dist in planets.items()]
        # Sort the list by distance
        planet_d.sort(key=lambda x: x[1])
        # Filter out all of the ones that are not between start_d and end_d
        filtered = list(filter(lambda x: start_d < x[1] < end_d, planet_d))
        # Return a tuple of just the planets
        return tuple(planet[0] for planet in filtered)
    except KeyError:
        return ()

