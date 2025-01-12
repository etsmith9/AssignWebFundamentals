import requests

# Task 2
def fetch_planet_data():
    response = requests.get('https://api.le-systeme-solaire.net/rest/bodies/')
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']: 
            name = planet['englishName']
            mass = planet['mass']['massValue'] if 'mass' in planet and planet['mass'] else None
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

            if mass is not None:
                planet_data.append({
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                })
    
    return planet_data

# Task 3
def find_heaviest_planet(planets):
    if not planets:
        return None, None

    heaviest_planet = max(planets, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


def main():
    planets = fetch_planet_data()  
    name, mass = find_heaviest_planet(planets)  
    
    if name and mass:
        print(f"The heaviest planet is {name} with a mass of {mass} kg.")
    else:
        print("No valid planet data found.")

main()