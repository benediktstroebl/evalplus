
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
    if not planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if not planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if planet1 == planet2:
        return []
    if not isinstance(planet1, str):
        return []
    if not isinstance(planet2, str):
        return []

    planet1 = planet1.lower()
    planet2 = planet2.lower()

    planets = []
    for planet in planet1, planet2:
        if "earth" in planet:
            for _, planet in enumerate(planet.split("earth")):
                planets.append(planet)
        elif "mercury" in planet:
            for _, planet in enumerate(planet.split("mercury")):
                planets.append(planet)
        elif "venus" in planet:
            for _, planet in enumerate(planet.split("venus")):
                planets.append(planet)
        elif "mars" in planet:
            for _, planet in enumerate(planet.split("mars")):
                planets.append(planet)
        elif "jupiter" in planet:
            for _, planet in enumerate(planet.split("jupiter")):
                planets.append(planet)
        elif "saturn" in planet:
            for _, planet in enumerate(planet.split("saturn")):
                planets.append(planet)
        elif "uranus" in planet:
            for _, planet in enumerate(planet.split("uranus")):
                planets.append(planet)
        elif "neptune" in planet:
            for _, planet in enumerate(planet.split("neptune")):
                planets.append(planet)
    return sorted(planets, key=lambda x: (x[0].distance(planet1
