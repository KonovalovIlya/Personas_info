import os
import pprint

data = [
    {
        'persona': 'Culebre',
        'Happy': ['N/A'],
        'Eager': ['Taunt (MC)', 'Pontificate']
    },
    {
        'persona': 'Cockatrice',
        'Happy': ['Persuade', 'Sing (MC)', 'Sarcasm', 'Flatter'],
        'Eager': ['Bribe', 'Ignore', 'Lie']
    },
    {
        'persona': 'Nue',
        'Happy': ['Persuade', 'Sing (MC)', 'Sarcasm', 'Flatter'],
        'Eager': ['Bribe', 'Ignore', 'Lie']
    },
    {
        'persona': 'Ocelot',
        'Happy': ['Persuade', 'Sing (MC)', 'Sarcasm', 'Flatter'],
        'Eager': ['Bribe', 'Ignore', 'Lie']
    },
    {
        'persona': 'Yomotsu Shikome',
        'Happy': ['Sing (MC)', 'Bribe', 'Sarcasm', 'Stare', 'Brag', 'Soothe', 'Joke', 'Seduce', 'Persuade (Yukino)', 'Scream'],
        'Eager': ['Abuse', 'Lie', 'Ignore']
    },
    {
        'persona': 'Cath Paluc',
        'Happy': ['Sing (MC)', 'Bribe', 'Sarcasm', 'Stare', 'Brag', 'Soothe', 'Joke', 'Seduce', 'Persuade (Yukino)', 'Scream'],
        'Eager': ['Abuse', 'Lie', 'Ignore']
    },
    {
        'persona': 'Purski',
        'Happy': ['Sing (MC)', 'Dance', 'Chat', 'Scold', 'Prestidigitate'],
        'Eager': ['Invite', 'Taunt']
    },
    {
        'persona': 'Titania',
        'Happy': ['Sing (MC)', 'Dance', 'Brag'],
        'Eager': ['Invite']
    },
    {
        'persona': 'Zombie Nurse',
        'Happy': ['Stare', 'Bully', 'Lie'],
        'Eager': ['Sarcasm']
    },
    {
        'persona': 'Picollus',
        'Happy': ['N/A'],
        'Eager': ['Persuade (MC)']
    },
    {
        'persona': 'Kwancha',
        'Happy': ['N/A'],
        'Eager': ['Persuade (MC)']
    },
    {
        'persona': 'Genkurou',
        'Happy': ['Plead', 'Lie', 'Cringe'],
        'Eager': ['Dance']
    },
    {
        'persona': 'Selket',
        'Happy': ['Sarcasm', 'Flatter', 'Prestidigitate'],
        'Eager': ['Stare']
    },
    {
        'persona': 'Anatomy',
        'Happy': ['Sing', 'Pontificate', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Pontificate', 'Abuse', 'Plead']
    },
    {
        'persona': 'Virtue',
        'Happy': ['Sing', 'Pontificate', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Pontificate', 'Abuse', 'Plead']
    },
    {
        'persona': 'Rakshasa',
        'Happy': ['Sarcasm', 'Prestidigitate'],
        'Eager': ['Taunt (MC)', 'Persuade (Yukino)']
    },
    {
        'persona': 'Malphas',
        'Happy': ['N/A'],
        'Eager': ['Persuade (MC)', 'Taunt (Mark)', 'Soothe']
    },
    {
        'persona': 'Tokebi',
        'Happy': ['Soothe', 'Bully', 'Persuade (Yukino)', 'Plead'],
        'Eager': ['Pontificate', 'Stare', 'Sing (Elly)', 'Pickup']
    },
    {
        'persona': 'Eligor',
        'Happy': ['Persuade (MC)', 'Pontificate', 'Sing (Elly)'],
        'Eager': ['Persuade (MC)', 'Stare']
    },
    {
        'persona': 'Ouroboros',
        'Happy': ['Persuade (MC)', 'Pontificate', 'Sing (Elly)'],
        'Eager': ['Persuade (MC)', 'Stare']
    },
    {
        'persona': 'Ocypete',
        'Happy': ['Pontificate', 'Sarcasm', 'Dance', 'Stare', 'Brag', 'Prestidigitate'],
        'Eager': ['Taunt (MC,Mark)', 'Stare', 'Brag', 'Chat', 'Cringe']
    },
    {   'persona': 'Celaeno',
        'Happy': ['Pontificate', 'Sarcasm', 'Dance', 'Stare', 'Brag', 'Prestidigitate'],
        'Eager': ['Taunt (MC,Mark)', 'Stare', 'Brag', 'Chat', 'Cringe']
    },
    {
        'persona': 'Aello',
        'Happy': ['Pontificate', 'Sarcasm', 'Dance', 'Stare', 'Brag', 'Prestidigitate'],
        'Eager': ['Taunt (MC,Mark)', 'Stare', 'Brag', 'Chat', 'Cringe']
    },
    {
        'persona': 'Jack Frost',
        'Happy': ['Persuade (MC)', 'Sing', 'Dance', 'Stare', 'Soothe', 'Cringe'],
        'Eager': ['Invite (MC)', 'Lie']
    },
    {
        'persona': 'Fuji Musume',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Invite (MC),Ignore (Reiji)']
    },
    {
        'persona': 'Rusalka',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Invite (MC),Ignore (Reiji)']
    },
    {
        'persona': 'Nekomata',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Invite (MC),Ignore (Reiji)']
    },
    {
        'persona': 'Slime',
        'Happy': ['Sing (MC)', 'Stare', 'Soothe', 'Invite (Elly)', 'Pickup', 'Seduce', 'Bully'],
        'Eager': ['Invite (MC)', 'Bribe', 'Cry']
    },
    {
        'persona': 'Zombie Girl',
        'Happy': ['Sing', 'Dance', 'Seduce', 'Persuade (Yukino)', 'Scream'],
        'Eager': ['Threaten', 'Ignore (Yukino,Reiji)']
    },
    {   'persona': 'Mr. Zombie',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Brag', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Seduce'],
        'Eager': ['Dance', 'Sing (Elly)', 'Threaten', 'Ignore']
    },
    {
        'persona': 'Zombie Boy',
        'Happy': ['Persuade (MC,Yukino)','Sing (MC)', 'Brag', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Seduce'],
        'Eager': ['Dance', 'Sing (Elly)', 'Threaten', 'Ignore']
    },
    {
        'persona': 'Ghost',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Brag', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Seduce'],
        'Eager': ['Dance', 'Sing (Elly)', 'Threaten', 'Ignore']
    },
    {
        'persona': 'Agathion',
        'Happy': ['Persuade (MC,Yukino)', 'Sing (MC)', 'Brag', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Seduce'],
        'Eager': ['Dance', 'Sing (Elly)', 'Threaten', 'Ignore']
    },
    {
        'persona': 'Nacht Kobold',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Hoodlum',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Afanc',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Ogre',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Phunbaba',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Zap',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Mizuchi',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Mushus',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Hecatoncheires',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Scold', 'Scream', 'Flatter'],
        'Eager': ['Bribe', 'Condescend', 'Sarcasm', 'Invite (Elly)', 'Startle', 'Threaten (Reiji)']
    },
    {
        'persona': 'Cu Sith',
        'Happy': ['Lie', 'Cringe', 'Scream', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Invite (MC)', 'Startle']
    },
    {
        'persona': 'Nisroc',
        'Happy': ['Lie', 'Cringe', 'Scream', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Invite (MC)', 'Startle']
    },
    {
        'persona': 'Teketeke',
        'Happy': ['Lie', 'Cringe', 'Scream', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Invite (MC)', 'Startle']
    },
    {
        'persona': 'Yaksini',
        'Happy': ['Sing (MC)', 'Pickup'],
        'Eager': ['Persuade (MC)', 'Invite (MC)', 'Chat', 'Startle']
    },
    {
        'persona': 'Dakini',
        'Happy': ['Sing (MC)', 'Pickup'],
        'Eager': ['Persuade (MC)', 'Invite (MC)', 'Chat', 'Startle']
    },
    {
        'persona': 'Knocker',
        'Happy': ['Invite (Elly)', 'Persuade (Yukino)'],
        'Eager': ['Sing (Elly)', 'Brag']
    },
    {
        'persona': 'Pixie',
        'Happy': ['Sing (MC)', 'Dance', 'Bribe', 'Persuade (Yukino)', 'Prestidigitate'],
        'Eager': ['Brag', 'Condescend', 'Abuse', 'Plead']
    },
    {
        'persona': 'Succubus',
        'Happy': ['Sing (MC)', 'Dance', 'Bribe', 'Persuade (Yukino)', 'Prestidigitate'],
        'Eager': ['Brag', 'Condescend', 'Abuse', 'Plead']
    },
    {
        'persona': 'Gandharva',
        'Happy': ['Bribe', 'Pontificate', 'Dance', 'Seduce', 'Horrify', 'Sing (Elly)', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Invite (Elly)', 'Taunt (Mark)', 'Stare', 'Brag', 'Abuse']
    },
    {
        'persona': 'Cupid',
        'Happy': ['Bribe', 'Pontificate', 'Dance', 'Seduce', 'Horrify', 'Sing (Elly)', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Invite (Elly)', 'Taunt (Mark)', 'Stare', 'Brag', 'Abuse']
    },
    {
        'persona': 'Otohime',
        'Happy': ['Sing (MC)', 'Dance', 'Pickup'],
        'Eager': ['Taunt (Mark)', 'Stare']
    },
    {
        'persona': 'Paimon',
        'Happy': ['Sing (MC)', 'Dance', 'Pickup'],
        'Eager': ['Taunt (Mark)', 'Stare']
    },
    {
        'persona': 'Yato no Kami',
        'Happy': ['Bully', 'Flatter'],
        'Eager': ['Persuade (MC)', 'Taunt (MC)', 'Stare', 'Joke', 'Cry', 'Threaten (Ayase,Reiji)', 'Cringe']
    },
    {
        'persona': 'Haokah',
        'Happy': ['Bully', 'Flatter'],
        'Eager': ['Persuade (MC)', 'Taunt (MC)', 'Stare', 'Joke', 'Cry', 'Threaten (Ayase,Reiji)', 'Cringe']
    },
    {
        'persona': 'Incubus',
        'Happy': ['Bully', 'Flatter'],
        'Eager': ['Persuade (MC)', 'Taunt (MC)', 'Stare', 'Joke', 'Cry', 'Threaten (Ayase,Reiji)', 'Cringe']
    },
    {
        'persona': 'Megaera',
        'Happy': ['Pickup', 'Bully'],
        'Eager': ['Cringe', 'Threaten (Ayase,Reiji)']
    },
    {
        'persona': 'Tisiphone',
        'Happy': ['Pickup', 'Bully'],
        'Eager': ['Cringe', 'Threaten (Ayase,Reiji)']
    },
    {
        'persona': 'Alecto',
        'Happy': ['Pickup', 'Bully'],
        'Eager': ['Cringe', 'Threaten (Ayase,Reiji)']
    },
    {
        'persona': 'Tlazolteotl',
        'Happy': ['Pickup', 'Bully'],
        'Eager': ['Cringe', 'Threaten (Ayase,Reiji)']
    },
    {
        'persona': 'Preta',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Ihika',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Ba',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Leprechaun',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Yaka',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Vetala',
        'Happy': ['Bribe', 'Sarcasm', 'Dance', 'Pickup', 'Bully', 'Persuade (Yukino)', 'Scold', 'Plead', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Dance', 'Sarcasm', 'Cry']
    },
    {
        'persona': 'Quicksilver',
        'Happy': ['Bribe', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Prestidigitate']
    },
    {
        'persona': 'Moh Shuvuu',
        'Happy': ['Bribe', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Prestidigitate']
    },
    {
        'persona': 'Iwate',
        'Happy': ['Bribe', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Prestidigitate']
    },
    {
        'persona': 'Scylla',
        'Happy': ['Bribe', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Prestidigitate']
    },
    {
        'persona': 'Kokkuri',
        'Happy': ['Pickup', 'Prestidigitate', 'Cringe'],
        'Eager': ['Condescend', 'Sarcasm', 'Brag', 'Invite (Elly)', 'Cry']
    },
    {
        'persona': 'Alastor',
        'Happy': ['Pickup', 'Prestidigitate', 'Cringe'],
        'Eager': ['Condescend', 'Sarcasm', 'Brag', 'Invite (Elly)', 'Cry']
    },
    {
        'persona': 'Hresvelgr',
        'Happy': ['Pickup', 'Prestidigitate', 'Cringe'],
        'Eager': ['Condescend', 'Sarcasm', 'Brag', 'Invite (Elly)', 'Cry']
    },
    {
        'persona': 'Hannya',
        'Happy': ['Bribe', 'Brag', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Sing (Elly)']
    },
    {
        'persona': 'Arachne',
        'Happy': ['Bribe', 'Brag', 'Pickup', 'Horrify', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Sing (Elly)']
    },
    {
        'persona': 'Zombie Painter',
        'Happy': ['Stare', 'Prestidigitate'],
        'Eager': ['Taunt (MC)', 'Stare']
    },
    {
        'persona': 'Hi no Enma',
        'Happy': ['Sarcasm', 'Horrify', 'Flatter', 'Scream', 'Prestidigitate'],
        'Eager': ['Taunt (MC)', 'Sarcasm', 'Stare']
    },
    {
        'persona': 'Sumizome',
        'Happy': ['Sarcasm', 'Horrify', 'Flatter', 'Scream', 'Prestidigitate'],
        'Eager': ['Taunt (MC)', 'Sarcasm', 'Stare']
    },
    {
        'persona': 'Zombie Cop',
        'Happy': ['Persuade (MC)', 'Horrify', 'Invite (Elly)', 'Bully', 'Flatter', 'Scream'],
        'Eager': ['Persuade (MC)', 'Plead']
    },
    {
        'persona': 'Power',
        'Happy': ['Persuade (MC)', 'Horrify', 'Invite (Elly)', 'Bully', 'Flatter', 'Scream'],
        'Eager': ['Persuade (MC)', 'Plead']
    },
    {
        'persona': 'Gdon',
        'Happy': ['Persuade (MC)', 'Horrify', 'Invite (Elly)', 'Bully', 'Flatter', 'Scream'],
        'Eager': ['Persuade (MC)', 'Plead']
    },
    {
        'persona': 'Lilim',
        'Happy': ['Flatter', 'Scream', 'Prestidigitate'],
        'Eager': ['Plead', 'Cringe']
    },
    {
        'persona': 'Yakuza',
        'Happy': ['Horrify', 'Sing (MC,Elly)', 'Soothe', 'Invite (Elly)', 'Flatter'],
        'Eager': ['Invite (MC)', 'Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Dribbler',
        'Happy': ['Horrify', 'Sing (MC,Elly)', 'Soothe', 'Invite (Elly)', 'Flatter'],
        'Eager': ['Invite (MC)', 'Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Archangel',
        'Happy': ['Horrify', 'Sing (MC,Elly)', 'Soothe', 'Invite (Elly)', 'Flatter'],
        'Eager': ['Invite (MC)', 'Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Yaksa',
        'Happy': ['Horrify', 'Sing (MC,Elly)', 'Soothe', 'Invite (Elly)', 'Flatter'],
        'Eager': ['Invite (MC)', 'Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Rukh',
        'Happy': ['Horrify', 'Sing (MC,Elly)', 'Soothe', 'Invite (Elly)', 'Flatter'],
        'Eager': ['Invite (MC)', 'Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Salome',
        'Happy': ['Sing (MC)', 'Pontificate', 'Brag', 'Pickup', 'Joke'],
        'Eager': ['Stare', 'Seduce', 'Threaten (Ayase)']
    },
    {
        'persona': 'Toufei',
        'Happy': ['Bribe'],
        'Eager': ['Sarcasm', 'Dance', 'Plead']
    },
    {
        'persona': 'Polisun',
        'Happy': ['Sing (MC)'],
        'Eager': ['Persuade (MC)', 'Brag']
    },
    {
        'persona': 'Jinn',
        'Happy': ['Sing (MC)'],
        'Eager': ['Persuade (MC)', 'Brag']
    },
    {
        'persona': 'Barbatos',
        'Happy': ['Sing (MC)'],
        'Eager': ['Persuade (MC)', 'Brag']
    },
    {
        'persona': 'Berith',
        'Happy': ['Pontificate', 'Dance'],
        'Eager': ['Condescend', 'Sarcasm']
    },
    {
        'persona': 'Fafnir',
        'Happy': ['Pontificate', 'Dance'],
        'Eager': ['Condescend', 'Sarcasm']
    },
    {
        'persona': 'Dark Elf',
        'Happy': ['Horrify'],
        'Eager': ['Sarcasm', 'Chat', 'Persuade (Yukino)']
    },
    {
        'persona': 'Black Widow',
        'Happy': ['Cringe', 'Prestidigitate'],
        'Eager': ['Stare']
    },
    {
        'persona': 'Druj',
        'Happy': ['Cringe', 'Prestidigitate'],
        'Eager': ['Stare']
    },
    {
        'persona': 'Principality',
        'Happy': ['Pontificate', 'Stare', 'Sing (Elly)', 'Soothe', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Stare', 'Soothe', 'Threaten (Reiji)']
    },
    {
        'persona': 'Naga',
        'Happy': ['Pontificate', 'Stare', 'Sing (Elly)', 'Soothe', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Stare', 'Soothe', 'Threaten (Reiji)']
    },
    {
        'persona': 'Dominion',
        'Happy': ['Pontificate', 'Stare', 'Sing (Elly)', 'Soothe', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Stare', 'Soothe', 'Threaten (Reiji)']
    },
    {
        'persona': 'Xiuhtecuhtli',
        'Happy': ['Pontificate', 'Stare', 'Sing (Elly)', 'Soothe', 'Prestidigitate'],
        'Eager': ['Persuade (MC)', 'Stare', 'Soothe', 'Threaten (Reiji)']
    },
    {
        'persona': 'Sarashina-hime',
        'Happy': ['Pontificate', 'Sarcasm'],
        'Eager': ['Stare', 'Threaten (Reiji,Ayase)']
    },
    {
        'persona': 'Rangda',
        'Happy': ['Pontificate', 'Sarcasm'],
        'Eager': ['Stare', 'Threaten (ReijiAyase)']
    },
    {
        'persona': 'Throne',
        'Happy': ['Pontificate', 'Sarcasm'],
        'Eager': ['Stare', 'Threaten (Reiji,Ayase)']
    },
    {
        'persona': 'Girimehkala',
        'Happy': ['Prestidigitate'],
        'Eager': ['Condescend']
    },
    {
        'persona': 'Pairika',
        'Happy': ['Prestidigitate', 'Sing (MC)'],
        'Eager': ['Plead', 'Chat', 'Sing (Elly)', 'Persuade (Yukino)']
    },
    {
        'persona': 'Pyro Jack',
        'Happy': ['Persuade (MC)', 'Flatter', 'Cringe'],
        'Eager': ['Invite (MC)', 'Lie']
    },
    {
        'persona': 'Ukobach',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Dance', 'Brag', 'Seduce', 'Cringe', 'Prestidigitate'],
        'Eager': ['Sing (Elly)', 'Cry', 'Lie', 'Threaten (Reiji)']
    },
    {
        'persona': 'Angel',
        'Happy': ['Persuade (MC,Yukino)', 'Bribe', 'Dance', 'Brag', 'Seduce', 'Cringe', 'Prestidigitate'],
        'Eager': ['Sing (Elly)', 'Cry', 'Lie', 'Threaten (Reiji)']
    },
    {
        'persona': 'Hanako',
        'Happy': ['Persuade (MC)', 'Sing (MC)', 'Bribe', 'Pickup', 'Joke', 'Lie', 'Cringe', 'Prestidigitate'],
        'Eager': ['Startle', 'Ignore (Reiji)']
    },
    {
        'persona': 'Nightmare',
        'Happy': ['Sing (MC)', 'Sarcasm', 'Invite (Elly)', 'Pickup', 'Seduce', 'Bully'],
        'Eager': ['Cry', 'Ignore (Yukino)', 'Lie', 'Threaten (Reiji)']
    },
    {
        'persona': 'Enku',
        'Happy': ['Sing (MC)', 'Sarcasm', 'Invite (Elly)', 'Pickup', 'Seduce', 'Bully'],
        'Eager': ['Cry', 'Ignore (Yukino)', 'Lie', 'Threaten (Reiji)']
    },
    {
        'persona': 'Catoblepas',
        'Happy': ['Sing (MC)', 'Sarcasm', 'Invite (Elly)', 'Pickup', 'Seduce', 'Bully'],
        'Eager': ['Cry', 'Ignore (Yukino)', 'Lie', 'Threaten (Reiji)']
    },
    {
        'persona': 'Bukimi',
        'Happy': ['Sing (MC)', 'Bribe', 'Sarcasm', 'Dance', 'Stare', 'Pickup', 'Chat', 'Seduce', 'Bully', 'Lie', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Ignore (Reiji)']
    },
    {
        'persona': 'Poltergeist',
        'Happy': ['Brag', 'Bribe', 'Sarcasm', 'Pickup', 'Soothe', 'Invite (Elly)', 'Seduce', 'Persuade (Yukino)'],
        'Eager': ['Bribe', 'Condescend', 'Invite (Elly)']
    },
    {
        'persona': 'Nozuchi',
        'Happy': ['Brag', 'Bribe', 'Sarcasm', 'Pickup', 'Soothe', 'Invite (Elly)', 'Seduce', 'Persuade (Yukino)'],
        'Eager': ['Bribe', 'Condescend', 'Invite (Elly)']
    },
    {
        'persona': 'Orthrus',
        'Happy': ['Persuade (MC)', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Flatter', 'Cringe', 'Scream'],
        'Eager': ['Taunt (MC)', 'Pickup', 'Invite (Elly)', 'Abuse']
    },
    {
        'persona': 'Ubelluris',
        'Happy': ['Persuade (MC)', 'Sarcasm', 'Invite (Elly)', 'Soothe', 'Seduce', 'Flatter', 'Cringe', 'Scream'],
        'Eager': ['Taunt (MC)', 'Pickup', 'Invite (Elly)', 'Abuse']
    },
    {
        'persona': 'Siren',
        'Happy': ['Sing (MC)', 'Pickup', 'Joke', 'Soothe'],
        'Eager': ['Stare', 'Brag', 'Seduce']
    },
    {
        'persona': 'Kobold',
        'Happy': ['Bribe', 'Stare', 'Persuade (Yukino)'],
        'Eager': ['Sarcasm', 'Stare', 'Abuse', 'Cry']
    },
    {
        'persona': 'Carrie',
        'Happy': ['Persuade (MC)', 'Bribe', 'Sarcasm', 'Horrify', 'Joke', 'Scream', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Dance', 'Invite (Elly)']
    },
    {
        'persona': 'Cromm Cruach',
        'Happy': ['Prestidigitate'],
        'Eager': ['Plead']
    },
    {
        'persona': 'Fenrir',
        'Happy': ['Prestidigitate'],
        'Eager': ['Plead']
    },
    {
        'persona': 'Cait Sith',
        'Happy': ['Sing (MC,Elly)', 'Pontificate', 'Soothe', 'Plead', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Stare', 'Brag', 'Invite (Elly)', 'Ignore (Reiji)', 'Threaten (Reiji)']
    },
    {
        'persona': 'Oberon',
        'Happy': ['Sing (MC,Elly)', 'Pontificate', 'Soothe', 'Plead', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Stare', 'Brag', 'Invite (Elly)', 'Ignore (Reiji)', 'Threaten (Reiji)']
    },
    {
        'persona': 'Ganesha',
        'Happy': ['Sing (MC,Elly)', 'Pontificate', 'Soothe', 'Plead', 'Prestidigitate'],
        'Eager': ['Sarcasm', 'Stare', 'Brag', 'Invite (Elly)', 'Ignore (Reiji)', 'Threaten (Reiji)']
    },
    {
        'persona': 'Gremlin',
        'Happy': ['Abuse'],
        'Eager': ['Plead']
    },
    {
        'persona': 'Shadow',
        'Happy': ['Sing (MC)', 'Stare', 'Plead', 'Prestidigitate'],
        'Eager': ['Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Andramelech',
        'Happy': ['Sing (MC)', 'Stare', 'Plead', 'Prestidigitate'],
        'Eager': ['Stare', 'Threaten (Ayase)']
    },
    {
        'persona': 'Duergar',
        'Happy': ['N/A'],
        'Eager': ['Bribe', 'Sarcasm']
    },
    {
        'persona': 'Doppleganger',
        'Happy': ['Persuade (MC)', 'Scream', 'Prestidigitate'],
        'Eager': ['Condescend', 'Chat', 'Persuade (Yukino)']
    },
    {
        'persona': 'Kiyohime',
        'Happy': ['Dance', 'Scold', 'Prestidigitate'],
        'Eager': ['Condescend', 'Chat', 'Persuade (Yukino)']
    },
    {
        'persona': 'Miyasudokoro',
        'Happy': ['Dance', 'Scold', 'Prestidigitate'],
        'Eager': ['Condescend', 'Chat', 'Persuade (Yukino)']
    },
    {
        'persona': 'Tengu',
        'Happy': ['Horrify', 'Prestidigitate'],
        'Eager': ['Soothe', 'Plead']
    },
    {
        'persona': 'Wyvern',
        'Happy': ['Sarcasm', 'Soothe', 'Invite (Elly)', 'Pickup', 'Seduce', 'Cringe', 'Prestidigitate'],
        'Eager': ['Cry', 'Cringe']
    },
    {
        'persona': 'Legion',
        'Happy': ['Prestidigitate'],
        'Eager': ['Dance', 'Cry']
    },
    {
        'persona': 'Kuchisake-onna',
        'Happy': ['Sarcasm', 'Pickup', 'Plead', 'Scream', 'Prestidigitate'],
        'Eager': ['N/A']
    }
]

def create_data():
    string = []

    file = os.path.abspath('personas.txt')
    with open (file, 'r') as f:
        string = [l.strip(' \n') for l in f.readlines()]

    list_personas = [string[i-2:i+1] for i, line in enumerate(string) if line.startswith('Eager')]

    dict_personas = []
    for j, k in enumerate(list_personas):
        #dict_personas[j] = {}
        dict_personas.append({'persona': k[0]})
        for item in k[1:]:
            key, value = item.split(': ')
            dict_personas[j][key] = value.split(', ')
    pprint.pp(dict_personas, indent=4)
    return dict_personas


def main(data):
    while True:
        persona = input('Введи название персоны:\n')
        if persona in ['x', 'X']:
            break
        for item in data:
            if item['persona'] == persona:
                print('Eager:', *item['Eager'], '\nHappy:', *item['Happy'])


if __name__ == '__main__':
    #data = create_data()
    main(data)
