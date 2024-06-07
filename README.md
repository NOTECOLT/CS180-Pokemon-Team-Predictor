# CS180-Pokemon-Team-Predictor

Authors:
Diego Eduardo A. Montenejo
Jayson Isaiah T. Tan

## About The Project

The Pokemon Team Predictor is a Machine Learning model that, when given an input of six pokemon, predicts the abilities, held items, and moves that each pokemon may most likely have.

### Dataset

The dataset used to train the predictor was taken from uploaded teams to Smogon Forums for Generation 9 OU. The dataset contains 1290 samples and was obtained through an online scraping tool, [Replay Scouter by FullLifeGames](https://fulllifegames.com/Tools/ReplayScouter/#/). The dataset contains 371 unique pokemon.

The datasets can be found within the [dataset](/datasets/) folder, which contains six files. These include:

- [raw_full_dataset.json](/datasets/raw_full_dataset.json) - This is the initial output scrapped using the Replay Scouter in json format. The json file contains a total of 1290 team data entries.

- [raw_full_dataset.json](/datasets/raw_full_dataset.csv) - This is the json data which has been lightly processed into .csv format for ease of readability. Each team has been split into six different data entries, one for each pokemon in the team, effectively multiplying the number of data entries to 7740. In each row contains each pokemon's ability, held item, moves, and team members.

- [preprocessed_input_dataset.csv](/datasets/preprocessed_input_dataset.csv) - This is the preprocssed input dataset containing all the original teams. The data contains only 2 columns, each pokemon and their team members from the previous file. One-hot encoding was applied on both features.

- [preprocessed_output_dataset.csv](/datasets/preprocessed_output_dataset.csv) - This is the output dataset containing each pokemon's ability, held item, and moves.

- [preprocessed_output_moves_training_dataset.csv](/datasets/preprocessed_output_moves_training_dataset.csv) - While both the existing `ability` and `item` features were directly inputted as the output class into the ML model, the `moves` column had to be processed further due to the nature of its data. Each data entry from the [preprocessed_output_dataset.csv](/datasets/preprocessed_output_dataset.csv) file was multipled once more by 4, for each move that each pokemon may have. One-hot encoding was then applied once again before the output `moves` class could be used by the classifier.

- [preprocessed_input_moves_training_dataset.csv](/datasets/preprocessed_input_moves_training_dataset.csv) - Likewise, each entry in the input moves dataset was also multiplied by 4. The are 30960 entries in each csv file.

Dataset preprocessing can be found in the [predictor-training.ipnyb](/predictor-training.ipynb) file.

## Model

The project uses three separate Complement Naive Bayes Classifiers to identify the most probable attributes of each pokemon. The models were created in Scikit-Learn The models can be found and loaded for yourself in the [models](/models/) folder. They are as follows:

- [ability_cnb.sav](/models/ability_cnb.sav) - Machine Learning model used to predict each pokemon's ability. The demo displays the ability that the pokemon is most likely to have given a set team.
  - Training Set Accuracy: 93.78%
  - Validation Set Accuracy: 92.55%

- [item_cnb.sav](/models/item_cnb.sav) - Machine Learning model used to predict each pokemon's held item. The demo displays the held item that the pokemon is most likely to have given a set team.
  - Training Set Accuracy: 62.44%
  - Validation Set Accuracy: 56.03%

- [moves_cnb.sav](/models/moves_cnb.sav) - Machine Learning model used to predict each pokemon's moves. The demo displays the top four moves that the pokemon is most likely to have given a set team.
  - Training Set Accuracy: 73.32%
  - Validation Set Accuracy: 66.00%

Model training can be found in the [predictor-training.ipnyb](/predictor-training.ipynb) file.

Overall, the model can usually predict the correct ability and at least 2 moves in the moveset of a pokemon. The held item is less accurate but it seems to at least pick a viable/popular choice of item for that pokemon. Since the model can only take from teams that were posted on the Smogon forum, the model cannot predict adaptations players would make to a current meta. Thus, unorthodox choices/sets are likely to not be predicted by the model. This is a weakness of the model since these niche choices could be specific, strategic choices made by the opposing player that could swing a match.

## Using the Program

In order to execute the demo, simply clone the project and `cd` into the folder the in which the repository was installed. Then, run `python predictor-demo.py` to run the project.

The program will ask you to enter the names of six pokemon. The input is case insensitive but must be typed exactly as formatted as found within the list of valid pokemon names (No spaces and no dashes). The full list can be found in the [Appendix](#appendix) below.

## References and Libraries Used

- [Replay Scouter by FullLifeGames](https://fulllifegames.com/Tools/ReplayScouter/#/)
- [Pandas - Python Data Analysis Library](https://pandas.pydata.org/)
- [SciKit-Learn](https://scikit-learn.org/)
- [NumPy](https://numpy.org/)

## Appendix

The following tables contain a full list of all valid pokemon names for the predictor. There are a total of 371 pokemon, with all names formatted to exclude any spaces or dashes. The predictor is case insensitive, so the input's capitalization does not need to follow the format of the names below.

### A - B

|  |  |  |  |  |
|---|---|---|---|---|
| Abomasnow | Alakazam | AlcremieSaltedCream | Alomomola | Altaria |
| AltariaMega | Amoonguss | Ampharos | Annihilape | Appletun |
| Araquanid | Arboliva | Arcanine | ArcanineHisui | Archaludon |
| Armarouge | ArticunoGalar | Avalugg | Azelf | Azumarill |
| Barraskewda | Basculegion | BasculegionF | Baxcalibur | Bellibolt |
| Bergmite | Bewear | Bisharp | Blaziken | Blissey |
| Brambleghast | Breloom | Bronzong | BruteBonnet |  |

### C

|  |  |  |  |  |
|---|---|---|---|---|
| Cacturne | Carbink | Carvanha | Centiskorch | Ceruledge |
| Cetitan | Chandelure | Chansey | Charizard | CharizardMegaY |
| Chesnaught | ChiYu | ChienPao | Cinccino | Cinderace |
| Clefable | Clodsire | Cloyster | Cobalion | Comfey |
| Conkeldurr | Copperajah | Corviknight | Crabominable | Cramorant |
| Crawdaunt | Cresselia | Croagunk | Crocalor | Cryogonal |
| Cyclizar |  |  |  |  |

### D

|  |  |  |  |  |
|---|---|---|---|---|
| Dachsbun | Darkrai | Darmanitan | DecidueyeHisui | Delibird |
| DeoxysDefense | DeoxysSpeed | Diancie | Dipplin | Ditto |
| Dolliv | Dondozo | Dragalge | Dragapult | Dragonair |
| Dragonite | Drednaw | Drifblim | Drifloon | Drowzee |
| Dudunsparce | Dugtrio | Dunsparce | Duraludon | Dusknoir |

### E - F

|  |  |  |  |  |
|---|---|---|---|---|
| Eelektross | Electivire | Empoleon | Enamorus | EnamorusTherian |
| Espathra | Espeon | Excadrill | ExeggutorAlola | Farigiraf |
| Feraligatr | Ferrothorn | Fezandipiti | Flamigo | Floatzel |
| Florges | FlorgesWhite | FlutterMane | Flygon | Forretress |
| Fraxure | Froslass | Frosmoth |  |  |

### G

|  |  |  |  |  |
|---|---|---|---|---|
| Gallade | Garchomp | Gardevoir | Garganacl | Gastrodon |
| GastrodonEast | Gengar | Gholdengo | Girafarig | Glaceon |
| Glastrier | Glimmet | Glimmora | Gliscor | Gogoat |
| Golduck | GolemAlola | Goodra | GoodraHisui | GougingFire |
| GourgeistSuper | Grafaiai | GreatTusk | Greninja | GreninjaBond |
| Grimmsnarl | Grookey | Gyarados |  |  |

### H - I

|  |  |  |  |  |
|---|---|---|---|---|
| Hatterene | Hattrem | Hawlucha | Haxorus | Heatran |
| Heracross | Hippopotas | Hippowdon | Hitmontop | HoopaUnbound |
| Houndstone | Hydrapple | Hydreigon | Incineroar | Indeedee |
| IndeedeeF | Infernape | IronBoulder | IronBundle | IronCrown |
| IronHands | IronJugulis | IronLeaves | IronMoth | IronThorns |
| IronTreads | IronValiant |  |  |  |

### J - L

|  |  |  |  |  |
|---|---|---|---|---|
| Jigglypuff | Jirachi | Keldeo | Kilowattrel | Kingambit |
| Kingdra | Kleavor | Klefki | Komala | Kommoo |
| Koraidon | Kyurem | LandorusTherian | Latias | LatiasMega |
| Latios | LatiosMega | Leafeon | Lechonk | Lilligant |
| LilligantHisui | Lokix | LopunnyMega | Lucario | Ludicolo |
| Luxray | Lycanroc | LycanrocDusk | LycanrocMidnight |  |

### M - N

|  |  |  |  |  |
|---|---|---|---|---|
| Magearna | Magneton | Magnezone | Mamoswine | Manaphy |
| Mandibuzz | Mareanie | Masquerain | Maushold | MausholdFour |
| Medicham | Melmetal | Meowscarada | Metagross | Mew |
| Milotic | Mimikyu | Misdreavus | Mismagius | Moltres |
| MoltresGalar | Mudsdale | MukAlola | Munkidori | Naclstack |
| Natu | Necrozma | Ninetales | NinetalesAlola | Noivern |
| Numel |  |  |  |  |

### O - P

|  |  |  |  |  |
|---|---|---|---|---|
| Ogerpon | OgerponCornerstone | OgerponHearthflame | OgerponWellspring | Okidogi |
| Oricorio | OricorioPomPom | OricorioSensu | Orthworm | Overqwil |
| Palafin | PalafinHero | Pawmot | Pawniard | Pecharunt |
| Pelipper | Pikachu | Pincurchin | Politoed | Poliwrath |
| Polteageist | PolteageistAntique | Primarina | Primeape | Pupitar |

### Q - R

|  |  |  |  |  |
|---|---|---|---|---|
| Quagsire | Quaquaval | Qwilfish | Rabsca | RagingBolt |
| Rapidash | Regieleki | Registeel | Reuniclus | Revavroom |
| Rhyperior | Ribombee | Rillaboom | RoaringMoon | Roserade |
| RotomFrost | RotomHeat | RotomWash |  |  |

### S

|  |  |  |  |  |
|---|---|---|---|---|
| Sableye | SableyeMega | Salamence | Salazzle | SamurottHisui |
| Sandaconda | SandslashAlola | SandyShocks | SawsbuckWinter | Scizor |
| ScizorMega | Scovillain | ScreamTail | Seismitoad | Serperior |
| Seviper | ShayminSky | Shellder | ShellosEast | Shiftry |
| Sinistcha | SinistchaMasterpiece | Skarmory | Skeledirge | Slaking |
| Sliggoo | SlitherWing | Slowbro | SlowbroGalar | SlowbroMega |
| Slowking | SlowkingGalar | Smeargle | Smoliv | Sneasler |
| Spidops | Spiritomb | Squawkabilly | Staraptor | Starmie |
| Stunfisk | Sudowoodo | Suicune | Sunkern | Swalot |
| Sylveon |  |  |  |  |

### T

|  |  |  |  |  |
|---|---|---|---|---|
| Talonflame | Tangrowth | TapuKoko | Tatsugiri | TatsugiriDroopy |
| TaurosPaldeaAqua | TaurosPaldeaBlaze | TaurosPaldeaFire | TaurosPaldeaWater | Tentacruel |
| Terapagos | TerapagosStellar | TerapagosTerastal | Thundurus | ThundurusTherian |
| TingLu | Tinkaton | Toedscool | Toedscruel | Togekiss |
| Torkoal | Tornadus | TornadusTherian | Torterra | Toxapex |
| Toxicroak | Toxtricity | ToxtricityLowKey | Tsareena | Tyranitar |

### U - Z

|  |  |  |  |  |
|---|---|---|---|---|
| Umbreon | Ursaluna | UrsalunaBloodmoon | Urshifu | UrshifuRapidStrike |
| Vaporeon | Veluza | Venusaur | Vespiquen | Victini |
| Volcanion | Volcarona | WalkingWake | Walrein | Weavile |
| WeezingGalar | WoChien | Zamazenta | ZamazentaCrowned | Zapdos |
| Zarude | Zeraora | Zoroark | ZoroarkHisui |  |
