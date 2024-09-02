
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
    from planet_functions import get_orbit_period
    
    # Define list of planet names
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    # Get planet1 orbit period
    orbit1 = get_orbit_period(planet1)
    
    # Get planet2 orbit period
    orbit2 = get_orbit_period(planet2)
    
    # Sort planets by orbit period
    planets.sort(key = lambda x: get_orbit_period(x))
    
    # Create empty list to store orbiting planets
    orbiting_planets = []
    
    # Get indices of orbiting planets
    for i in range(len(planets)):
        if orbit1 < get_orbit_period(planets[i]) < orbit2:
            orbiting_planets.append(planets[i])
    
    # Check if planet1 and planet2 are in list
    if planet1 not in orbiting_planets:
        print("Planet " + planet1 + " is not a planet name.")
        return
    if planet2 not in orbiting_planets:
        print("Planet " + planet2 + " is not a planet name.")
        return
    
    # If planet1 and planet2 are in list, return list
    return orbiting_planets

