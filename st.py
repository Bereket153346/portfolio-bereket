import streamlit as st
from email.mime.text import MIMEText

# Configuration de la page
st.set_page_config(page_title="Portfolio de Bereket", page_icon="🔧", layout="wide")

# Fonction pour afficher les liens sociaux
def afficher_liens():
    st.markdown(
        """
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
            <a href="https://github.com" target="_blank" style="color: #0366d6; text-decoration: none; font-weight: bold;">GitHub</a>
            <a href="https://linkedin.com" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: bold;">LinkedIn</a>
            <a href="https://root-me.org" target="_blank" style="color: #d00000; text-decoration: none; font-weight: bold;">Root-Me</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contenu principal
menu = ["Accueil", "Parcours Académique", "Certifications", "CV"]
choice = st.radio("", menu, horizontal=True)

if choice == "Accueil":
    st.title("Futur Ingénieur en Cybersécurité et Réseaux")

    # Mise en page
    col1, col2 = st.columns([1, 2])

    with col1:
        # Afficher la photo dans le rectangle réservé
        photo_path = "image/photo_perso.jpg"  # Chemin correct vers l'image
        try:
            import base64

            # Charger l'image et la convertir en base64
            with open(photo_path, "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

            # Afficher l'image dans un cadre défini
            st.markdown(
                f"""
                <div style="width: 250px; height: 300px; border: 2px solid #333; border-radius: 10px; 
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); background-color: #f4f4f4; overflow: hidden; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <img src="data:image/png;base64,{img_base64}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 10px;" alt="Photo">
                </div>
                """,
                unsafe_allow_html=True,
            )
        except FileNotFoundError:
            st.markdown(
                """
                <div style="width: 250px; height: 300px; border: 2px solid #333; border-radius: 10px; 
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); background-color: #f4f4f4; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <p style="color: #888; font-style: italic;">Image introuvable</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Ajouter les informations de contact avec un espacement uniforme
        st.markdown(
            """  
            📍 **Adresse** : 102 Rue de Verdun, Villejuif  
            📧 **Email** : [berekettkelesi@gmail.com](mailto:berekettkelesi@gmail.com)  
            📞 **Téléphone** : +33 6 12 34 56 78
            """,
            unsafe_allow_html=True,
        )

        # Ajouter les liens alignés avec les informations de contact
        st.markdown(
            """
            <div style="margin-top: 15px; display: flex; justify-content: flex-start; gap: 15px;">
                <a href="https://github.com" target="_blank" style="color: #0366d6; text-decoration: none; font-weight: bold;">GitHub</a>
                <a href="https://linkedin.com" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: bold;">LinkedIn</a>
                <a href="https://root-me.org" target="_blank" style="color: #d00000; text-decoration: none; font-weight: bold;">Root-Me</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        # Section "À propos de moi"
        st.markdown(
            """
            <div style="background-color: #222; padding: 15px; border-radius: 10px; margin-top: 20px; 
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);">
                <h4 style="color: #f05454;">À propos de moi</h4>
                <p style="color: white;">Passionné par la sécurité informatique, je suis actuellement en 4ème année à l'EFREI Paris, spécialisé en Cybersécurité et Réseaux.</p>
                <p style="color: white;">Je recherche une alternance de 12 mois à partir de septembre 2025.</p>
                <p style="color: white;">Je suis une personne motivée, toujours à la recherche de nouveaux défis.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Ajouter la section "COMPÉTENCES" en bas
        st.markdown(
            """
            <div style="background-color: #222; padding: 15px; border-radius: 10px; margin-top: 20px; 
            box-shadow: 0 0 10px rgba(0, 0, 255, 0.3);">
                <h4 style="color: #42a5f5;">COMPÉTENCES</h4>
                <div style="display: flex; flex-direction: row; justify-content: space-between; margin-top: 10px;">
                    <div style="width: 48%; color: white;">
                        <h5 style="color: #42a5f5;">🔧 Techniques</h5>
                        <ul>
                            <li>Réseaux informatiques : TCP/IP, DNS, DHCP, VPN</li>
                            <li>Sécurité informatique : Pentesting, analyse de vulnérabilités</li>
                            <li>Frameworks : Metasploit (MSF), Assessment Methodologies</li>
                            <li>Programmation : Python, Java, C++</li>
                            <li>Outils : Wireshark, Burp Suite, Nmap, Metasploit</li>
                            <li>Virtualisation : Docker, VMware</li>
                            <li>Cloud et Réseaux : Azure, Unifi, Cisco, OVH</li>
                        </ul>
                    </div>
                    <div style="width: 48%; color: white;">
                        <h5 style="color: #42a5f5;">🌐 Langues</h5>
                        <ul>
                            <li>Français : niveau courant</li>
                            <li>Anglais : niveau courant</li>
                            <li>Amharique : langue maternelle</li>
                        </ul>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )




elif choice == "Parcours Académique":
    st.header("🎓 Parcours Académique")
    
    # Section EFREI Paris et Innovafeed côte à côte
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            margin-bottom: 20px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.2); display: flex; align-items: center; gap: 15px;">
                <div>
                    <h4 style="color: #e57373; margin-bottom: 10px;">EFREI Paris</h4>
                    <p style="color: white;">2020 - 2022 : Prépa intégrée</p>
                    <p style="color: white;">2023 - 2025 : Alternance chez Innovafeed</p>
                    <p style="color: white;">2026 : Diplôme d'ingénieur en Cybersécurité et Réseaux</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            box-shadow: 0 0 10px rgba(255, 165, 0, 0.2); display: flex; align-items: center; gap: 15px;">
                <div>
                    <h4 style="color: #ffa726; margin-bottom: 10px;">Alternance chez Innovafeed</h4>
                    <p style="color: white;"><strong>Dates :</strong> 2023 - 2025</p>
                    <p style="color: white;"><strong>Compétences :</strong></p>
                    <ul style="color: white;">
                        <li>Gestion des réseaux informatiques</li>
                        <li>Développement d'infrastructures sécurisées</li>
                        <li>Surveillance et détection des anomalies</li>
                    </ul>
                    <p style="color: white;"><strong>Projets :</strong></p>
                    <ul style="color: white;">
                        <li>Automatisation des processus</li>
                        <li>Renforcement de la sécurité réseau</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    # Afficher le rectangle du lycée en bas
    st.markdown("---")  # Ligne de séparation
    st.markdown(
        """
        <div style="background-color: #000; padding: 20px; border-radius: 10px; margin-top: 20px; 
        box-shadow: 0 0 10px rgba(0, 0, 255, 0.2);">
            <h4 style="color: #42a5f5;">Lycée Marcellin Berthelot</h4>
            <p style="color: white;"><strong>Baccalauréat général :</strong></p>
            <ul style="color: white;">
                <li>Mathématiques</li>
                <li>Physique-Chimie</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif choice == "Certifications":
    st.header("📜 Certifications")

    # Certifications validées
    col1, col2 = st.columns(2)
    with col1:
        # Certification CCNA1
        st.markdown(
            """
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            margin-bottom: 20px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);">
                <h4 style="color: #42a5f5;">Network Architecture: CCNA1</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Certification Stormshield Network Administrator
        st.markdown(
            """
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            margin-bottom: 20px; box-shadow: 0 0 10px rgba(0, 0, 255, 0.5);">
                <h4 style="color: #42a5f5;">Stormshield Network Administrator</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        # Certification eJPT
        st.markdown(
            f"""
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            margin-bottom: 20px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);">
                <h4 style="color: #42a5f5;">INE : Certification eJPT</h4>
                <a href="https://certs.ine.com/4b91cbe8-1150-4dec-ab2e-005ae8c40a5b#acc.wL7ngE2O" target="_blank" style="color: #42a5f5; text-decoration: none; font-weight: bold;">Voir le certificat</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Certification Gestion de Projet
        st.markdown(
            f"""
            <div style="background-color: #000; padding: 20px; border-radius: 10px; 
            margin-bottom: 20px; box-shadow: 0 0 10px rgba(0, 0, 255, 0.5);">
                <h4 style="color: #42a5f5;">Gestion de Projet</h4>
                <a href="https://moocgdp.gestiondeprojet.pm/certificates/1e10af53ef324f4a9bf57139b5107fea" target="_blank" style="color: #42a5f5; text-decoration: none; font-weight: bold;">Voir le certificat</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Certifications en cours
    st.markdown("---")
    st.header("📌 Certifications en cours")
    st.markdown(
        """
        <div style="background-color: #000; padding: 20px; border-radius: 10px; 
        box-shadow: 0 0 10px rgba(255, 165, 0, 0.5);">
            <h4 style="color: #ffa726;">Certifications en cours :</h4>
            <ul style="color: white;">
                <li>eCPPT</li>
                <li>CEH</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif choice == "CV":
    st.header("📄 Mon CV")
    try:
        # Chemin du fichier PDF
        cv_path = "CV_Bereket_Tadiwos.pdf"

        with open(cv_path, "rb") as cv_file:
            # Télécharger le fichier
            st.download_button(
                label="📥 Télécharger mon CV",
                data=cv_file,
                file_name="Bereket_Tadiwos_CV.pdf",
                mime="application/pdf",
            )

        # Convertir le PDF en base64 pour affichage
        import base64

        with open(cv_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
            pdf_display = f"""
            <div style="border: 2px solid #ff4d4d; border-radius: 10px; width: 855px; height: 800px; margin: auto; 
                        padding: 10px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.5); overflow: hidden;">
                <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="100%" style="border: none;"></iframe>
            </div>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("Le fichier du CV est introuvable. Veuillez vérifier son emplacement.")



