import streamlit as st
import base64


# Configuration de la page
st.set_page_config(page_title="Portfolio de Bereket", page_icon="🔧", layout="wide")

# Fonction pour afficher les liens sociaux



# Contenu principal
menu = ["Accueil", "Parcours Académique", "Certifications", "CV", "Projets & Compétences"]

# Ajouter des styles personnalisés pour un design incroyable
st.markdown(
    """
    <style>
    div.stRadio > div {
        display: flex;
        justify-content: center;
        gap: 15px;
        background: linear-gradient(145deg, #2e2e2e, #1c1c1c);
        border-radius: 12px;
        padding: 10px 20px;
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    div.stRadio > div > label {
        font-size: 16px;
        color: #e0e0e0;
        background-color: #333;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    div.stRadio > div > label:hover {
        background-color: #444;
        color: #ff8800;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(255, 136, 0, 0.5);
    }
    div.stRadio > div > label[data-selected="true"] {
        background: linear-gradient(145deg, #ff4d4d, #d32f2f);
        color: white;
        box-shadow: 0 6px 12px rgba(255, 77, 77, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menu radio avec styles modernes
choice = st.radio("", menu, horizontal=True)


if choice == "Accueil":
    st.markdown(
        """
        <h1 style="text-align: center; color: white; font-size: 2.5em; margin-bottom: 20px;">
            Futur Ingénieur en Cybersécurité et Réseaux
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Mise en page
    col1, col2 = st.columns([1, 2])

    with col1:
        # Afficher la photo dans le rectangle réservé (sans animation)
        photo_path = "image/photo_perso.jpg"  # Chemin correct vers l'image
        try:
            # Charger l'image et la convertir en base64
            with open(photo_path, "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

            # Afficher l'image dans un cadre défini (sans animation)
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
            <div style="margin-top: 5px; display: flex; justify-content: flex-start; gap: 10px;">
                <a href="https://github.com" target="_blank" style="color: #0366d6; text-decoration: none; font-weight: bold;">GitHub</a>
                <a href="https://linkedin.com" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: bold;">LinkedIn</a>
                <a href="https://root-me.org" target="_blank" style="color: #d00000; text-decoration: none; font-weight: bold;">Root-Me</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Ajouter une section pour les langues parlées (avec animation)
        st.markdown(
            """
            <div style="margin-top: 10px; padding: 10px; background-color: #1c1c1c; border-radius: 30px; 
            animation: alternateBoxShadow 12s infinite;">
                <h4 style="color: #42a5f5;">🌍 Langues parlées</h4>
                <ul style="color: white; list-style-type: none; padding-left: 0;">
                    <li>🇫🇷 Français : Niveau courant</li>
                    <li>🇬🇧 Anglais : Niveau courant</li>
                    <li>🇪🇹 Amharique : Langue maternelle</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        # Section "À propos de moi" (avec animation)
        st.markdown(
    """
    <div style="background-color:#1c1c1c; padding: 15px; border-radius: 30px; margin-top: 10px; 
    animation: alternateBoxShadow 12s infinite;">
        <h4 style="color: #f05454;">À propos de moi</h4>
        <p style="color: white;">
            Passionné par la cybersécurité et les réseaux, je suis actuellement étudiant en 4ème année à l'EFREI Paris, une école d'ingénieurs reconnue pour son excellence en informatique et technologies.
        </p>
        <p style="color: white;">
            Au-delà de mes études, je m'investis pleinement dans le développement de mes compétences techniques et humaines. Mon objectif est de devenir un expert en cybersécurité, capable de protéger les infrastructures numériques tout en apportant des solutions innovantes.
        </p>
        <p style="color: white;">
            Je suis à la recherche d'une alternance de 12 mois, à partir de septembre 2025, pour m'immerger dans des projets concrets, relever des défis techniques, et continuer à apprendre aux côtés de professionnels expérimentés. Je crois fermement que chaque opportunité est une chance d'exceller, de collaborer et de contribuer de manière significative.
        </p>
        <p style="color: white;">
            Motivé, curieux et résilient, je suis prêt à relever les défis du monde professionnel et à apporter mon énergie et ma détermination à une équipe dynamique et ambitieuse.
        </p>
        <p style="color: white; font-style: italic;">
            "Rien n'est impossible pour celui qui a la volonté d'apprendre et de se dépasser." – C'est avec cette conviction que je me prépare à écrire mon prochain chapitre professionnel.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

        # Ajouter le rectangle animé avec des messages alternants
        st.markdown(
            """
            <style>
            @keyframes alternateBoxShadow {
                0%, 33% { box-shadow: 0 20px 6px rgba(0, 0, 255, 0.3); }
                34%, 66% { box-shadow: 0 20px 6px rgba(255, 0, 0, 0.3); }
                67%, 100% { box-shadow: 0 20px 6px rgba(255, 165, 0, 0.3); }
            }
            .animated-box {
                padding: 20px;
                border-radius: 30px;
                background-color: #1c1c1c;
                animation: alternateBoxShadow 12s infinite; 
                color: white;
                text-align: center;
                margin-top: 40px;
            }
            .message {
                display: inline-block;
                animation: fadeInOut 20s linear infinite;
            }

            @keyframes fadeInOut {
                0%, 25% { opacity: 1; }
                50%, 100% { opacity: 0; }
            }
            </style>

            <div class="animated-box">
                <span class="message" style="animation-delay: 0s;">
                    Je suis à la recherche d'une alternance de 12 mois à partir de septembre 2025, dans le domaine de la cybersécurité et réseaux, pour améliorer mes compétences.
                </span>
                <span class="message" style="animation-delay: 10s;">
                    I am looking for a 12-month internship starting in September 2025, in the field of cybersecurity and networks, to improve my skills.
                </span>
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
            <style>
            @keyframes alternateBoxShadow {
                0%, 33% { box-shadow: 0 20px 6px rgba(0, 0, 255, 0.3); }
                34%, 66% { box-shadow: 0 20px 6px rgba(255, 0, 0, 0.3); }
                67%, 100% { box-shadow: 0 20px 6px rgba(255, 165, 0, 0.3); }
            }
            </style>
            <div style="background-color: #1c1c1c; padding: 30px; border-radius: 30px; 
            margin-bottom: 20px; animation: alternateBoxShadow 12s infinite; display: flex; align-items: center; gap: 15px;">
                <div>
                    <h4 style="color: #e57373; margin-bottom: 5px;">EFREI Paris</h4>
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
            <div style="background-color: #1c1c1c; padding: 20px; border-radius: 30px; 
            animation: alternateBoxShadow 12s infinite; display: flex; align-items: center; gap: 15px;">
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
        <div style="background-color: #1c1c1c; padding: 20px; border-radius: 30px; margin-top: 20px; 
        animation: alternateBoxShadow 12s infinite;">
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

    # Ajouter les styles pour l'animation des couleurs
    st.markdown(
        """
        <style>
        @keyframes alternateBoxShadow {
            0%, 33% { box-shadow: 0 20px 6px rgba(0, 0, 255, 0.3); }
            34%, 66% { box-shadow: 0 20px 6px rgba(255, 0, 0, 0.3); }
            67%, 100% { box-shadow: 0 20px 6px rgba(255, 165, 0, 0.3); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Certifications validées
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ff4d4d;">Network Architecture: CCNA1</h4>
                <p style="color: #bbbbbb;">Certification Cisco Networking Academy, <strong>CCNA1</strong> </p>
            </div>
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ff4d4d;">Stormshield Network Administrator</h4>
                <p style="color: #bbbbbb;">Certification Stormshield Network Administrator.</p>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ff4d4d;">INE : Certification eJPT</h4>
                <p style="color: #bbbbbb;">La certification eJPT, conçue pour les débutants, 
                valide mes compétences en tests de pénétration, incluant l'audit 
                des systèmes et la sécurité des réseaux, hôtes et applications web.
                  Une belle première étape dans le domaine de la cybersécurité.</p>
                <a href="https://certs.ine.com/4b91cbe8-1150-4dec-ab2e-005ae8c40a5b#acc.wL7ngE2O" target="_blank" 
                   style="display: inline-block; padding: 8px 18px; background-color: #ff4d4d; 
                          color: #fff; text-decoration: none; border-radius: 5px; 
                          box-shadow: 0 4px 6px rgba(255, 0, 0, 0.5); font-size: 14px;">
                   Voir le certificat
                </a>
            </div>
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ff4d4d;">Gestion de Projet</h4>
                <p style="color: #bbbbbb;">Certification en gestion de projet. Cette certification montre que j'ai acquis les bases de la gestion de projet, comme la planification,
                  l'organisation et la coordination, pour mener à bien des projets.</p>
                <a href="https://moocgdp.gestiondeprojet.pm/certificates/1e10af53ef324f4a9bf57139b5107fea" target="_blank" 
                   style="display: inline-block; padding: 8px 18px; background-color: #ff4d4d; 
                          color: #fff; text-decoration: none; border-radius: 5px; 
                          box-shadow: 0 4px 6px rgba(255, 0, 0, 0.5); font-size: 14px;">
                   Voir le certificat
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Certifications en cours
    st.markdown("---")
    st.header("📌 Certifications en cours")
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ffa726;">eCPPT</h4>
                <p style="color: #bbbbbb;">Certification en cours de préparation.</p>
            </div>
            <div style="flex: 1; margin: 10px; padding: 15px; border-radius: 30px; 
                        animation: alternateBoxShadow 12s infinite; background-color: #1c1c1c;">
                <h4 style="color: #ffa726;">CEH</h4>
                <p style="color: #bbbbbb;">Certification en cours de préparation.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif choice == "CV":
    st.header("📄 Mon CV")

    # Ajouter les styles pour l'animation des couleurs
    st.markdown(
        """
        <style>
        @keyframes alternateBoxShadow {
            0%, 33% { box-shadow: 0 0 60px rgba(255, 0, 0, 0.5); }
            34%, 66% { box-shadow: 0 0 60px rgba(0, 0, 255, 0.5); }
            67%, 100% { box-shadow: 0 0 60px rgba(255, 165, 0, 0.5); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Chemin du fichier PDF pour le téléchargement
    pdf_path = "CV_Bereket_Tadiwos.pdf"
    # Chemin de l'image PNG pour l'affichage
    png_path = "image/Bereket_Tadiwos_CV-1.png"

    try:
        # Lire et afficher l'image PNG (CV sous forme d'image avec encadrement)
        with open(png_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode("utf-8")
            st.markdown(
                f"""
                <div style="border: 2px solid #ff4d4d; border-radius: 10px; width: 600px; height: 800px; margin: auto; 
                            padding: 10px; animation: alternateBoxShadow 12s infinite; overflow: hidden; text-align: center;">
                    <img src="data:image/png;base64,{img_base64}" alt="CV" style="max-width: 100%; height: 100%; object-fit: contain; border-radius: 10px;">
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Ajouter un bouton pour télécharger le fichier PDF
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Télécharger mon CV (PDF)",
                data=pdf_file,
                file_name="Bereket_Tadiwos_CV.pdf",
                mime="application/pdf",
            )

    except FileNotFoundError:
        st.error("Le fichier du CV ou de l'image est introuvable. Veuillez vérifier leur emplacement.")

    
elif choice == "Projets & Compétences":
    st.header("🚀 Mes Projets et Compétences")

    # Ajouter les styles pour l'animation des couleurs
    st.markdown(
        """
        <style>
        @keyframes alternateBoxShadow {
            0%, 33% { box-shadow: 0 20px 6px rgba(255, 0, 0, 0.3); }
            34%, 66% { box-shadow: 0 20px 6px rgba(0, 0, 255, 0.3); }
            67%, 100% { box-shadow: 0 20px 6px rgba(255, 165, 0, 0.3); }
        }
        .animated-box {
            animation: alternateBoxShadow 12s infinite;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Section "Compétences"
    st.subheader("💡 Compétences")
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div class="animated-box" style="flex: 1; margin: 10px; padding: 20px; border-radius: 30px; 
                        background-color: #1c1c1c;">
                <h4 style="color: #ff5733;">🔧 Techniques</h4>
                <ul>
                    <li><strong>Réseaux informatiques</strong> : TCP/IP, DNS, VPN</li>
                    <li><strong>Programmation </strong> : Python, Java, C++</li>
                    <li><strong>Frameworks </strong>: Metasploit, Docker, VMware</li>
                    <li><strong>Sécurité informatique </strong>: Pentesting, analyse de vulnérabilités</li>
                    <li><strong>Outils </strong>: Wireshark, Burp Suite, Nmap, Metasploit</li>
                    <li><strong>Virtualisation </strong>: Docker, VMware</li>
                    <li><strong>Cloud et Réseaux </strong> : Azure, Unifi, Cisco, OVH</li>   
                </ul>
            </div>
            <div class="animated-box" style="flex: 1; margin: 10px; padding: 20px; border-radius: 30px; 
                        background-color: #1c1c1c;">
                <h4 style="color: #007bff;">🛠️ Outils utilisés</h4>
                <ul>
                    <li><strong>Malwarebytes</strong> : Protection et analyse des systèmes</li>
                    <li><strong>Primo</strong> : Gestion des ordinateurs et périphériques</li>
                    <li><strong>Google Workspace</strong> : Outils collaboratifs utilisés dans un cadre professionnel</li>
                    <li><strong>Kali Linux</strong> : Utilisation pour l'entraînement aux tests d'intrusion et au pentesting</li>
                    <li><strong>WatchGuard Firewalls</strong> : Gestion et supervision des pare-feu, avec analyse approfondie des flux réseau </li>
                    <li><strong>Stormshield</strong> : Configuration et gestion des pare-feux</li>
                    <li><strong>Microsoft Office 365</strong> : Bureautique avancée</li>
                    <li><strong>Unifi Wi-Fi Deployment</strong> : Configuration et gestion des bornes Unifi</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section "Projets"
    st.subheader("📁 Mes Projets")
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div class="animated-box" style="flex: 1; margin: 10px; padding: 20px; border-radius: 30px; 
                        background-color: #1c1c1c;">
                <h4 style="color: #ffffff;">Graph_Encrypt</h4>
                <p style="color: #bbbbbb;">Chiffrement des données avec des graphes via l'algo de Kruskal. Dans ce projet, nous avons développé un algorithme de chiffrement et de déchiffrement en utilisant la théorie des graphes, et plus précisément l'algorithme de Kruskal pour générer un arbre couvrant minimal. Cet algorithme permet de sécuriser les données en exploitant les propriétés mathématiques des graphes, garantissant ainsi une méthode de chiffrement originale et efficace. L'approche repose sur la minimisation des coûts à travers l'arbre couvrant, ce qui renforce la sécurité tout en maintenant une performance optimale. Ce projet illustre une utilisation innovante de concepts théoriques appliqués à la cybersécurité. </p>
                <a href="https://github.com/Bereket153346/Graph_Encrypt.git" target="_blank" 
                   style="display: inline-block; padding: 10px 20px; background-color: #ff0000; 
                          color: #fff; text-decoration: none; border-radius: 5px;">
                   Voir sur GitHub
                </a>
            </div>
            <div class="animated-box" style="flex: 1; margin: 10px; padding: 20px; border-radius: 30px; 
                        background-color: #1c1c1c;">
                <h4 style="color: #ffffff;">Détection d'Intrusion</h4>
                <p style="color: #bbbbbb;">Détection des attaques réseau avec des modèles machine learning. Dans ce projet, j'ai développé un système de détection d'intrusions réseau en utilisant des techniques de machine learning. J'ai travaillé sur un dataset contenant des données de trafic réseau capturées, comprenant des connexions normales et des attaques classées en quatre catégories principales : DoS, Probe, R2L et U2R. Chaque connexion était décrite par 41 caractéristiques, comme la durée, le protocole utilisé, ou le nombre de connexions vers d'autres hôtes. Mon objectif était de construire un modèle capable de classifier efficacement ces activités réseau. Cela a impliqué plusieurs étapes, notamment la préparation des données, le choix des algorithmes adaptés et l'optimisation des hyperparamètres pour améliorer la précision du modèle final.</p>
                <a href="https://github.com/Bereket153346/intrusion_detection_machine_learning.git" target="_blank" 
                   style="display: inline-block; padding: 10px 20px; background-color: #ff0000; 
                          color: #fff; text-decoration: none; border-radius: 5px;">
                   Voir sur GitHub
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
