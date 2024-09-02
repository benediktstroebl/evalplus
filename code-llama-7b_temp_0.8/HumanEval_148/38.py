
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
    # Please print the function's output
    # Example:
    # print(bf("Mars", "Earth"))
    # >>> ("Venus")
    
    # Planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Orbits
    orbits = {
        "Mercury": 0,
        "Venus": 1,
        "Earth": 2,
        "Mars": 3,
        "Jupiter": 4,
        "Saturn": 5,
        "Uranus": 6,
        "Neptune": 7
    }
    
    # Check if input is correct
    if planet1 in planets and planet2 in planets:
        # Sort all planets by orbit
        planets_orbits = list(zip(orbits.values(), orbits.keys()))
        # Sort list by orbit
        planets_orbits.sort()
        # Get the indices of the planets
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        # Get the planets between the orbit of the two given planets
        planets_between_orbit = planets_orbits[idx1:idx2]
        # Get the planets between the orbit of the two given planets
        planets_between_orbit = [x for _, x in planets_between_orbit]
        return planets_between_orbit
    else:
        return ()
