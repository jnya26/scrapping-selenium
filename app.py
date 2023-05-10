from services import SocialNetworkScrapper

if __name__ == "__main__":
    service = SocialNetworkScrapper()
    service.social_network_login()
    service.create_post()
    print("done")