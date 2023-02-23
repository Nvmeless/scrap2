# ensure you have Python (3  or latest)
# ensure you have pip installer

from Scraper import Scraper
from Studyrama import Studyrama

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.studyrama.com'
uri = "/formations/annuaire-des-formations?btnRechercherFormations=rechercher&page="

studyramaInstance = Studyrama(baseUrl, uri, 1)
studyramaInstance2 = Studyrama(baseUrl, uri, 2)

scraper1 = Scraper(studyramaInstance2, "linksListStudy.csv", "infosStudy.csv")
scraper = Scraper(studyramaInstance, "linksList.csv", "infos.csv")

scraper.exec()
scraper1.exec()

print("Done")