
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
    # Planets = list of planets
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # Get index for planet1
    p1 = planets.index(planet1)
    # Get index for planet2
    p2 = planets.index(planet2)
    # Create a list of tuples with a planet's orbit, planet's orbit's position
    # relative to the sun and the distance to the sun.
    #tuple = (planet, orbit, distance)
    # t[0] = planet, 
    # t[1] = orbit,
    # t[2] = distance
    t = [(planets[i], planets[i], abs(i - p1)) for i in range(len(planets))]
    # Remove all tuples that are not in the range [p1, p2]
    t = [x for x in t if x[1] >= p1 and x[1] <= p2]
    # Sort the remaining tuples by distance to earth
    t = sorted(t, key = lambda x: x[2])
    # Return the tuples in the desired order
    return tuple(x[0] for x in t)
