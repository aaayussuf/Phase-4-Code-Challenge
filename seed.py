from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Seed heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]
    db.session.add_all(heroes)
    db.session.commit()

    # Seed powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    db.session.add_all(powers)
    db.session.commit()

    # Seed hero_powers
    hero_powers = [
        HeroPower(hero_id=1, power_id=1, strength="Strong"),
        HeroPower(hero_id=1, power_id=2, strength="Average"),
        HeroPower(hero_id=2, power_id=1, strength="Weak"),
        HeroPower(hero_id=3, power_id=3, strength="Average"),
        HeroPower(hero_id=4, power_id=4, strength="Strong"),
        HeroPower(hero_id=5, power_id=3, strength="Strong"),
        HeroPower(hero_id=6, power_id=2, strength="Average"),
        HeroPower(hero_id=7, power_id=1, strength="Weak"),
        HeroPower(hero_id=8, power_id=4, strength="Average"),
        HeroPower(hero_id=9, power_id=3, strength="Strong"),
        HeroPower(hero_id=10, power_id=1, strength="Average")
    ]
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Database seeded successfully!")