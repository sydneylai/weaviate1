# The Weaviate Challenge

## Create a Weaviate pipeline and build a showcase app for presentation

For this project: build a workflow and a front-end application to display the final result.

## Introduction

### Getting Started
Dependencies:
* Python 3.8 or higher
* Weaviate Python Client
* Your preferred library for vector generation (e.g., TensorFlow, PyTorch, etc.)

## Usage:

### Test 1: import.py

In this file, I got started with: 

1. [Weaviate's Quickstart Tutorial](https://weaviate.io/developers/weaviate/quickstart)
2. Using Weaviate's Readers & Generators modules: [Generative Search - OpenAI](https://weaviate.io/developers/weaviate/modules/reader-generator-modules/generative-openai) 


This allowed for me to become familiarized with the Weaviate developer environment. I was **able to install Wevaite and Hugging Face's sample database**.

![Screen Shot 2023-07-31 at 4 22 36 PM](https://github.com/sydneylai/weaviate1/assets/7811907/be6b0964-d566-4ac9-a8e3-048cb0db39c7)


I was **unable to identify the syntax error and therefore unable to install Generative Search - OpenAI**.

### Test 2: assets.py

**Submission: Vector Search for RPG Game Assets with Weaviate**
This project demonstrates how to use Weaviate, a cloud-native, modular, real-time vector search engine, to manage and search through RPG game assets like inventory items.

The project I wanted to educate developers on how to create a system to manage and search through RPG game assets like inventory items, loot, gear, and power-ups using Weaviate, as a cloud-native, modular, real-time vector search engine.

In this build, there is a list of game assets. Each of these assets is a piece of metadata that would include various properties like type (e.g., weapon, armor, potion), rarity (common, uncommon, rare, legendary), stats (damage, defense, health boost, etc.), and perhaps a short description.

The data might not be in a format that's easy to search through efficiently. This is where the Weaviate integration comes in. I demonstrate how Weaviate uses vector embeddings to represent complex data in a way that can be efficiently searched.

This repo includes Python script that handles the vectorization of game assets, adding them to Weaviate, and querying the database for similar assets.

### Challenges Faced
Along the way, I faced some challenges such as:

1. Integrating a build with external Generators
2. Project scoping, the time I initially allocated for this was underestimated given the project's complexity


### Presentation

1. Lessons learned
2. Showcase current version of the build
3. Explore additional developer activations

[[Google Slides]](https://docs.google.com/presentation/d/1JpRIkGYauLSosW9UOAIwSg_h1YxwMHhhMmCHDKAVcZQ/edit?usp=sharing)
