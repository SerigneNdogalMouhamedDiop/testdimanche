"""
Utilisation des dictionnaires
pour la gestion des services
"""
def afficher_service(services):
    try:
        port = int(input("Entrez un numéro de port : "))
        # .get() permet de gérer le cas où la clé n'existe pas
        service = services.get(port)

        if service is None:
            print(f"Aucun service connu pour le port {port}.")
        else:
            print(f"Port {port} -> Service : {service}")

    except ValueError:
        print("Entrée invalide : veuillez saisir un nombre.")

def menu():
    # Dictionnaire de base (exemples)
    services = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        53: "DNS",
        21: "FTP",
        25: "SMTP"
    }

    while True:
        print("\n--- Menu services réseau ---")
        print("1) Chercher le service d'un port")
        print("2) Afficher tous les ports/services")
        print("3) Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher_service(services)
        elif choix == "2":
            # Affichage trié par port
            for port in sorted(services):
                print(f"{port} -> {services[port]}")
        elif choix == "3":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    menu()
