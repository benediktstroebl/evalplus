
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
    # Check that both planet1 and planet2 are correct planet names
    if planet1.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return []
    if planet2.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return []

    # Initialize an empty list
    planets = []

    # Add each planet to the list if its orbit is between the orbits of planet1 and planet2
    if planet1 == "mercury":
        planets.append("Venus")
        planets.append("Earth")
        planets.append("Mars")
        planets.append("Jupiter")
        planets.append("Saturn")
        planets.append("Uranus")
        planets.append("Neptune")
    elif planet1 == "venus":
        planets.append("Earth")
        planets.append("Mars")
       
