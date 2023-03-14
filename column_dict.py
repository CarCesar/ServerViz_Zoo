# declarations of useful variables

# english translation dictionnary
import json
import os
import pandas as pd


column_dict_reptiles = {
  'catalog_number': {'type': int, 'file_name': 'NumeroDeCatalogo', 'selected': True},
  'cataloged_date':{'type': str, 'file_name': 'DataDeEntrada', 'selected': False},
  'determined_date':{'type': str, 'file_name': 'DataDaDeterminacao', 'selected': False},
  'collected_date':{'type': str, 'file_name': 'DataColetaInicial', 'selected': False},
  'year_cataloged':{'type': int, 'file_name': 'ano_entrada', 'selected': True},
  'month_cataloged':{'type': int, 'file_name': 'mes_entrada', 'selected': True},
  'month_determined':{'type': int, 'file_name': 'mes_determinacao', 'selected': True},
  'year_collected':{'type': int, 'file_name': 'ano_coleta', 'selected': True},
  'month_collected':{'type': int, 'file_name': 'mes_coleta', 'selected': True},
  'class':{'type': str, 'file_name': 'Class', 'selected': True},
  'kingdom':{'type': str, 'file_name': 'Kingdom', 'selected': True},
  'genus_old':{'type': str, 'file_name': 'Genero_ent', 'selected': False},
  'genus':{'type': str, 'file_name': 'Genero_atual', 'selected': True},
  'species_old':{'type': str, 'file_name': 'Especie_ent', 'selected': True},
  'species':{'type': str, 'file_name': 'Especie_atual', 'selected': True},
  'subspecies':{'type': str, 'file_name': 'Subespecie_atual', 'selected': True},
  'subspecies_old':{'type': str, 'file_name': 'Subespecie_ent', 'selected': True},
  'type_status':{'type': str, 'file_name': 'type_status', 'selected': True},
  'determinator_full_name':{'type': str, 'file_name': 'DeterminatorFirst_and_LastName1', 'selected': True},
  'collector_full_name':{'type': str, 'file_name': 'CollectorFirst_and_LastName1', 'selected': True},
  'altitude':{'type': float, 'file_name': 'altitude', 'selected': True},
  'max_altitude':{'type': float, 'file_name': 'max_altitude', 'selected': True},
  'order':{'type': str, 'file_name': 'Ordem', 'selected': True},
  'suborder':{'type': str, 'file_name': 'Subordem', 'selected': True},
  'family':{'type': str, 'file_name': 'Familia', 'selected': True},
  'phylum':{'type': str, 'file_name': 'Phylum', 'selected': True},
  'qualifier':{'type': str, 'file_name': 'Qualificador_atual', 'selected': True},
  'lat':{'type': float, 'file_name': 'Lat', 'selected': True},
  'long':{'type': float, 'file_name': 'Long', 'selected': True},
  'municipio':{'type': str, 'file_name': 'Municipio', 'selected': True},
  'state':{'type': str, 'file_name': 'EstadoOuProvincia', 'selected': True},
  'country':{'type': str, 'file_name': 'Pais', 'selected': True},
  'continent':{'type': str, 'file_name': 'Continente', 'selected': True},
  'region':{'type': str, 'file_name': 'region', 'selected': True},
  'lost_in_fire':{'type': int, 'file_name': 'lost_in_fire', 'selected': True},
  'year_determined':{'type': int, 'file_name': 'year_determined', 'selected': True},
  'author_full':{'type': str, 'file_name': 'author_full', 'selected': False},
  'first_author':{'type': str, 'file_name': 'first_author', 'selected': False},
}


column_dict_crustacea = {
  'catalog_number': {'type': int, 'file_name': 'CatalogNumber', 'selected': True},
  'cataloged_date':{'type': str, 'file_name': 'Cataloged Date', 'selected': False},
  'determined_date':{'type': str, 'file_name': '', 'selected': False},
  'collected_date':{'type': str, 'file_name': 'Start Date', 'selected': False},
  'year_cataloged':{'type': int, 'file_name': '', 'selected': True},
  'month_cataloged':{'type': int, 'file_name': '', 'selected': True},
  'month_determined':{'type': int, 'file_name': '', 'selected': True},
  'year_collected':{'type': int, 'file_name': '', 'selected': True},
  'month_collected':{'type': int, 'file_name': '', 'selected': True},
  'class':{'type': str, 'file_name': 'Class1', 'selected': True},
  'kingdom':{'type': str, 'file_name': 'Kingdom', 'selected': True},
  'genus_old':{'type': str, 'file_name': '', 'selected': False},
  'genus':{'type': str, 'file_name': 'Genus1', 'selected': True},
  'species_old':{'type': str, 'file_name': '', 'selected': False},
  'species':{'type': str, 'file_name': 'Species1', 'selected': True},
  'subspecies':{'type': str, 'file_name': '', 'selected': False},
  'subspecies_old':{'type': str, 'file_name': '', 'selected': False},
  'type_status':{'type': str, 'file_name': 'Type Status1', 'selected': True},
  'determinator_full_name':{'type': str, 'file_name': 'determinator_full_name1', 'selected': True},
  'collector_full_name':{'type': str, 'file_name': 'collector_full_name1', 'selected': True},
  'min_depth':{'type': float, 'file_name': 'StartDepth', 'selected': True},
  'max_depth':{'type': float, 'file_name': 'EndDepth', 'selected': True},
  'order':{'type': str, 'file_name': 'Order1', 'selected': True},
  'suborder':{'type': str, 'file_name': 'Suborder1', 'selected': True},
  'family':{'type': str, 'file_name': 'Family1', 'selected': True},
  'phylum':{'type': str, 'file_name': 'Phylum1', 'selected': True},
  'qualifier':{'type': str, 'file_name': 'Qualifier1', 'selected': True},
  'lat':{'type': float, 'file_name': 'Latitude1', 'selected': True},
  'long':{'type': float, 'file_name': 'Longitude1', 'selected': True},
  'municipio':{'type': str, 'file_name': '', 'selected': False},
  'state':{'type': str, 'file_name': 'State', 'selected': True},
  'country':{'type': str, 'file_name': 'Country', 'selected': True},
  'continent':{'type': str, 'file_name': 'Continent', 'selected': True},
  'region':{'type': str, 'file_name': 'County', 'selected': True},
  'lost_in_fire':{'type': int, 'file_name': '', 'selected': False},
  'year_determined':{'type': int, 'file_name': '', 'selected': True},
  'author_full':{'type': str, 'file_name': '', 'selected': False},
  'first_author':{'type': str, 'file_name': '', 'selected': False},
  'infraorder':{'type': str, 'file_name': 'Infraorder1', 'selected': True},
  'locality':{'type': str, 'file_name': 'Locality Name', 'selected': True},


}

column_dict_polychaete = {
  # Dados Temporais
  'catalog_number':{'type':str,'file_name':'Catalog Number','selected': True},
  'cataloged_date':{'type': str, 'file_name': 'Cataloged Date', 'selected': False}, 
  #'determined_date':{'type': str, 'file_name': 'Cataloged Date' , 'selected': False},#'Determined date 1', 'selected': False},
  'collected_date':{'type': str, 'file_name': 'Start Date', 'selected': False},
  'year_cataloged':{'type': int, 'file_name': '', 'selected': True},
  'month_cataloged':{'type': int, 'file_name': '', 'selected': True},
  #'year_determined':{'type': int, 'file_name': '', 'selected': True},
  #'month_determined':{'type': int, 'file_name': '', 'selected': True},
  'year_collected':{'type': int, 'file_name': '', 'selected': True},
  'month_collected':{'type': int, 'file_name': '', 'selected': True},
  # Dados Geograficos
  'lat':{'type': float, 'file_name': 'Latitude', 'selected': True},
  'long':{'type': float, 'file_name': 'Longitude', 'selected': True},
  'municipio':{'type': str, 'file_name': '', 'selected': False},
  'state':{'type': str, 'file_name': 'State', 'selected': True},
  'country':{'type': str, 'file_name': 'Country', 'selected': True},
  'continent':{'type': str, 'file_name': 'Continent', 'selected': True},
  'region':{'type': str, 'file_name': 'County', 'selected': True},
  'locality':{'type': str, 'file_name': 'Locality Name', 'selected': True},
    # Profundidade
  'min_depth':{'type': float, 'file_name': 'Min Depth', 'selected': True},
  'max_depth':{'type': float, 'file_name': 'Max Depth', 'selected': True},
  # Dados Cientificos
  'kingdom':{'type': str, 'file_name': 'Kingdom', 'selected': True},
  'phylum':{'type': str, 'file_name': 'Phylum 1', 'selected': True},
  'class':{'type': str, 'file_name': 'Class 1', 'selected': True},
  'order':{'type': str, 'file_name': 'Order 1', 'selected': True},
  #'suborder':{'type': str, 'file_name': 'Suborder1', 'selected': True},
  'family':{'type': str, 'file_name': 'Family 1', 'selected': True},
  'genus_old':{'type': str, 'file_name': '', 'selected': False},
  'genus':{'type': str, 'file_name': 'Genus 1', 'selected': True},
  'species_old':{'type': str, 'file_name': '', 'selected': False},
  'species':{'type': str, 'file_name': 'Species 1', 'selected': True},
  'subspecies':{'type': str, 'file_name': '', 'selected': False},
  'subspecies_old':{'type': str, 'file_name': '', 'selected': False},
  'type_status':{'type': str, 'file_name': 'Type Status 1', 'selected': True},
  'qualifier':{'type': str, 'file_name': 'Qualifier 1', 'selected': True},
  # Dados dos Cientistas
  'determinator_full_name':{'type': str, 'file_name': 'Determiner 1  complete name', 'selected': True},
  'determinator_full_name2':{'type': str, 'file_name': 'Determiner 2 complete name', 'selected': True},
  'determinator_full_name3':{'type': str, 'file_name': 'Determiner 3 complete name', 'selected': True},
  'collector_full_name':{'type': str, 'file_name': 'collector complete name 1', 'selected': True},
  'author_full':{'type': str, 'file_name': '', 'selected': False},
  'first_author':{'type': str, 'file_name': '', 'selected': False},
  'lost_in_fire':{'type': int, 'file_name': '', 'selected': False},
}

column_dict_polychaete_MN = {
  # Dados Temporais
  'catalog_number':{'type':str,'file_name':'Catalog Number','selected': True},
  'cataloged_date':{'type': str, 'file_name': 'Cataloged Date', 'selected': False}, ###############
  #'determined_date':{'type': str, 'file_name': 'Cataloged Date' , 'selected': False},#'Determined date 1', 'selected': False},
  'collected_date':{'type': str, 'file_name': 'Start Date', 'selected': False},
  'year_cataloged':{'type': int, 'file_name': '', 'selected': True},
  'month_cataloged':{'type': int, 'file_name': '', 'selected': True},
  #'year_determined':{'type': int, 'file_name': '', 'selected': True},
  #'month_determined':{'type': int, 'file_name': '', 'selected': True},
  'year_collected':{'type': int, 'file_name': '', 'selected': True},
  'month_collected':{'type': int, 'file_name': '', 'selected': True},
  # Dados Geograficos
  'lat':{'type': float, 'file_name': 'Latitude1', 'selected': True},
  'long':{'type': float, 'file_name': 'Longitude1', 'selected': True},
  'municipio':{'type': str, 'file_name': '', 'selected': False},
  'state':{'type': str, 'file_name': 'State', 'selected': True},
  'country':{'type': str, 'file_name': 'Country', 'selected': True},
  'continent':{'type': str, 'file_name': 'Continent', 'selected': True},
  'region':{'type': str, 'file_name': 'County', 'selected': True},
  'locality':{'type': str, 'file_name': 'Locality Name', 'selected': True},
    # Profundidade
  'min_depth':{'type': float, 'file_name': 'Min Depth', 'selected': True},
  'max_depth':{'type': float, 'file_name': 'Max Depth', 'selected': True},
  # Dados Cientificos
  'kingdom':{'type': str, 'file_name': 'Kingdom', 'selected': True},
  'phylum':{'type': str, 'file_name': 'Phylum 1', 'selected': True},
  'class':{'type': str, 'file_name': 'Class 1', 'selected': True},
  'order':{'type': str, 'file_name': 'Order 1', 'selected': True},
  #'suborder':{'type': str, 'file_name': 'Suborder1', 'selected': True},
  'family':{'type': str, 'file_name': 'Family 1', 'selected': True},
  'genus_old':{'type': str, 'file_name': '', 'selected': False},
  'genus':{'type': str, 'file_name': 'Genus 1', 'selected': True},
  'species_old':{'type': str, 'file_name': '', 'selected': False},
  'species':{'type': str, 'file_name': 'Species 1', 'selected': True},
  'subspecies':{'type': str, 'file_name': '', 'selected': False},
  'subspecies_old':{'type': str, 'file_name': '', 'selected': False},
  'type_status':{'type': str, 'file_name': 'Type Status 1', 'selected': True},
  'qualifier':{'type': str, 'file_name': 'Qualifier 1', 'selected': True},
  # Dados dos Cientistas
  'determinator_full_name':{'type': str, 'file_name': 'Determiner Complete Name', 'selected': True},
  'collector_full_name':{'type': str, 'file_name': 'Collector 1 complete name', 'selected': True},
  'author_full':{'type': str, 'file_name': '', 'selected': False},
  'first_author':{'type': str, 'file_name': '', 'selected': False},
  'lost_in_fire':{'type': int, 'file_name': '', 'selected': False},
}


column_dict_GBIF = {
  'catalog_number': {'type': int, 'file_name': 'catalogNumber', 'selected': True},
  'cataloged_date':{'type': str, 'file_name': '', 'selected': False},
  'determined_date':{'type': str, 'file_name': 'dateIdentified', 'selected': False},
  'collected_date':{'type': str, 'file_name': 'eventDate', 'selected': False},
  'year_cataloged':{'type': int, 'file_name': '', 'selected': False},
  'month_cataloged':{'type': int, 'file_name': '', 'selected': False},
  'month_determined':{'type': int, 'file_name': '', 'selected': True},
  'year_collected':{'type': int, 'file_name': '', 'selected': True},
  'month_collected':{'type': int, 'file_name': '', 'selected': True},
  'kingdom':{'type': str, 'file_name': 'kingdom', 'selected': True},
  'phylum':{'type': str, 'file_name': 'Phylum1', 'selected': True},
  'class':{'type': str, 'file_name': 'class', 'selected': True},
  'order':{'type': str, 'file_name': 'order', 'selected': True},
  'family':{'type': str, 'file_name': 'family', 'selected': True},
  'genus_old':{'type': str, 'file_name': '', 'selected': False},
  'genus':{'type': str, 'file_name': 'genus', 'selected': True},
  'species_old':{'type': str, 'file_name': '', 'selected': False},
  'species':{'type': str, 'file_name': 'species', 'selected': True},
  'subspecies':{'type': str, 'file_name': '', 'selected': False},
  'subspecies_old':{'type': str, 'file_name': '', 'selected': False},
  'type_status':{'type': str, 'file_name': 'typeStatus', 'selected': True},
  'determinator_full_name':{'type': str, 'file_name': 'identifiedBy', 'selected': True},
  'collector_full_name':{'type': str, 'file_name': 'recordedBy', 'selected': True},
  'min_depth':{'type': float, 'file_name': 'depth', 'selected': True},
  'altitude':{'type': float, 'file_name': 'elevation', 'selected': True},
  'qualifier':{'type': str, 'file_name': 'Qualifier1', 'selected': False},
  'lat':{'type': float, 'file_name': 'decimalLatitude', 'selected': True},
  'long':{'type': float, 'file_name': 'decimalLongitude', 'selected': True},
  'municipio':{'type': str, 'file_name': '', 'selected': False},
  'state':{'type': str, 'file_name': 'stateProvince', 'selected': True},
  'country':{'type': str, 'file_name': 'countryCode', 'selected': True},
  'continent':{'type': str, 'file_name': '', 'selected': False},
  'region':{'type': str, 'file_name': '', 'selected': False},
  'lost_in_fire':{'type': int, 'file_name': '', 'selected': False},
  'year_determined':{'type': int, 'file_name': '', 'selected': True},
  'author_full':{'type': str, 'file_name': '', 'selected': False},
  'first_author':{'type': str, 'file_name': '', 'selected': False},
  'locality':{'type': str, 'file_name': 'locality', 'selected': True},

}

def get_selected_columns():
  return {
  'catalog_number': True,
  'year_collected': True,
  'month_collected': True,
  'class': True,
  'order': True,
  'family': True,
  'genus': True,
  'type_status': True,
  'determinator_full_name': True,
  'collector_full_name': True,
  'min_depth': True,
  'altitude': True,
  'lat': True,
  'long': True,
  'state': True,
  'country': True,
}

def get_custom_mapping():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  json_path = os.path.join('ressources','custom_mapping.csv')

  file_path = os.path.join(root_dir,json_path)

  return pd.read_csv(file_path, index_col=False, header=0)

custom_mapping = get_custom_mapping()