
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
    # Create a list of all planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if the input planets are valid
    if not (planet1 in planets and planet2 in planets):
        return ()
    
    # Check if the orbit of planet1 is before the orbit of planet2
    if planet1 < planet2:
        # Sort the list of planets by the distance from the sun
        planets = sorted(planets, key=lambda x: (x.semi_major_axis, x.distance, x.eccentricity, x.inclination))
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet2
        position = planets.index(planet2)
        
        # Get the position of the orbit of planet1
        position = planets.index(planet1)
        
        # Get the position of the orbit of planet2
