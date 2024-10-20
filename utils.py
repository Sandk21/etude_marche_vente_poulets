# Crée les boxplots de chacune des colonnes du dataframe
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def boxplot_columns(df: pd.DataFrame) -> go.Figure:
    """Crée des boxplots dans des graphiques séparés pour toute les colonnes d'un dataframe

    Args:
        df (pd.DataFrame): Dataframe à analyser

    Returns: 
        Graph plotply
    """

    # Exclusion des colonnes non numériques
    df_num =  df.select_dtypes(include=['number'])

    # Déterminer le nombre de colonnes d'export à tracer
    export_columns = [col for col in df_num.columns]

    # Création de la figure avec plusieurs sous-graphes
    fig = make_subplots(rows=1, cols=len(export_columns), subplot_titles=export_columns)

    # Ajout des traces aux sous-graphes
    for i, col in enumerate(export_columns):
        trace = go.Box(
            y=df[col], 
            name=col, 
            boxpoints='all',  # Affiche tous les points
            hovertext=df.index
        )
        fig.add_trace(trace, row=1, col=i+1)

    # Mise en forme des sous-graphes
    fig.update_layout(
        width=1700,  # Largeur de la figure en pixels
        height=600   # Hauteur de la figure en pixels
    )

    # Affichage du graphique
    fig.show()