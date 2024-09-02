
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
    # Open file with Solar System data
    with open('solar_system.txt', 'r') as f:
        data = f.read()
    # Split data into planets
    planets = data.split('\n')
    # Remove first line (empty)
    planets.pop(0)
    # Remove last line (empty)
    planets.pop()
    # Initialize empty list to store planets
    planet_list = []
    # Iterate over planets
    for planet in planets:
        # Get position and name of planet
        pos, name = planet.split()
        # Check if the position is valid
        if 800 <= float(pos) <= 1000:
            # Check if name is valid
            if name == 'Mercury' or name == 'Venus' or name == 'Earth' or name == 'Mars' or name == 'Jupiter' or name == 'Saturn' or name == 'Uranus' or name == 'Neptune':
                # Add position and name to list
                planet_list.append(pos)
                planet_list.append(name)
            else:
                return ()
    # Sort list by distance from the sun
    sorted_list = sorted(planet_list, key=lambda x: float(x[0]))
    # Return list of closest planets
    return sorted_list
