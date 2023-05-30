{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "mount_file_id": "13c4kbQDK3K11l3kuTLeb5t-tNpf8Fi8Q",
      "authorship_tag": "ABX9TyNifmIBIjqnO5e85WzTUEde",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Dontin84/repo/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O_ZduVHktpsM"
      },
      "outputs": [],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "st.write(\"\"\"#Hello World This is my **first** *app*! \"\"\")"
      ],
      "metadata": {
        "id": "xNdPefHNuA1g"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Add a title\n",
        "st.title(\"My Streamlit App\")\n",
        "\n",
        "# Add text\n",
        "st.header(\"Welcome to my Streamlit app!\")\n",
        "st.subheader(\"Here are some examples of Streamlit features:\")\n",
        "\n",
        "# Add an image\n",
        "st.image(\"https://via.placeholder.com/400\", caption=\"Streamlit Logo\")\n",
        "\n",
        "# Add a button\n",
        "if st.button(\"Click me\"):\n",
        "    st.write(\"Button clicked!\")\n",
        "\n",
        "# Add a checkbox\n",
        "show_data = st.checkbox(\"Show data\")\n",
        "if show_data:\n",
        "    # Create sample data\n",
        "    data = pd.DataFrame({\n",
        "        \"Name\": [\"John\", \"Emma\", \"Michael\", \"Sophia\"],\n",
        "        \"Age\": [25, 30, 35, 28],\n",
        "        \"Country\": [\"USA\", \"UK\", \"Canada\", \"Australia\"]\n",
        "    })\n",
        "    # Display the data\n",
        "    st.write(\"Sample Data:\")\n",
        "    st.dataframe(data)\n",
        "\n",
        "# Add a plot\n",
        "st.header(\"Data Visualization\")\n",
        "st.subheader(\"Histogram Example\")\n",
        "# Generate random data\n",
        "data = pd.DataFrame({'values': [2, 4, 6, 8, 10]})\n",
        "# Plot the data\n",
        "plt.hist(data['values'])\n",
        "st.pyplot(plt)\n",
        "\n",
        "# Add a sidebar\n",
        "st.sidebar.header(\"Sidebar\")\n",
        "option = st.sidebar.selectbox(\"Select an option\", [\"Option 1\", \"Option 2\", \"Option 3\"])\n",
        "\n",
        "st.sidebar.write(\"You selected:\", option)\n",
        "\n",
        "# Run the app\n",
        "if __name__ == \"__main__\":\n",
        "  st.write()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "IrXHvVXOZCyx",
        "outputId": "80fce97d-747c-46d5-d3fe-0cc3055f3e7e"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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TZumtWvXqr29XTk5OZKk+fPnKy4uTiUlJZKkzMxMlZaWasqUKUpNTdXhw4e1fPlyZWZmdkcJAAC4cHkdI1lZWTp+/LiKiorU1NSkyZMna8eOHd03tTY0NPS4EnLfffcpKChI9913n44eParLL79cmZmZevDBB313FgAAwG95HSOSlJeXp7y8vF4fq66u7nmA0FAVFxeruLi4P4cCAAABju+mAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKaIEQAAYIoYAQAApogRAABgihgBAACmiBEAAGCKGAEAAKb6FSNlZWVKSEhQeHi4UlNTVVtbe9btT548qdzcXMXExMjlcunqq6/W9u3b+zUwAAAILKHe7lBRUaGCggKVl5crNTVVa9euVUZGhg4ePKioqKgztu/s7NT3vvc9RUVF6YUXXlBcXJw+/PBDDR061BfzAwAAP+d1jJSWlmrRokXKycmRJJWXl2vbtm3auHGjli5desb2Gzdu1CeffKLXX39dF110kSQpISHhm00NAAAChldv03R2dqqurk7p6elfPUFwsNLT01VTU9PrPi+++KLS0tKUm5srt9utCRMmaNWqVerq6urzOB0dHWptbe2xAACAwORVjJw4cUJdXV1yu9091rvdbjU1NfW6z5EjR/TCCy+oq6tL27dv1/Lly7VmzRo98MADfR6npKREQ4YM6V7i4+O9GRMAAPiRAf80jcfjUVRUlNavX6/k5GRlZWVp2bJlKi8v73OfwsJCtbS0dC+NjY0DPSYAADDi1T0jw4cPV0hIiJqbm3usb25uVnR0dK/7xMTE6KKLLlJISEj3unHjxqmpqUmdnZ0KCws7Yx+X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w5wnnnjCegyfamtrc6666iqnsrLSuf766538/HzrkXymuLjYSUpKsh5jwNxzzz3Otddeaz3GeZWfn++MGTPG8Xg81qP4xOzZs50FCxb0WPejH/3ImTdvntFEvnX69GknJCTEeemll3qsnzp1qrNs2TKjqXxHkrNly5buP3s8Hic6Otr5zW9+073u5MmTjsvlcp577rkBn+eCvDLy/7W0tEiSLr30UuNJfK+rq0ubN29We3t7wP0K/tzcXM2ePVvp6enWowyId999V7GxsRo9erTmzZunhoYG65F85sUXX1RKSopuueUWRUVFacqUKdqwYYP1WAOms7NTf/rTn7RgwQKfftmnpenTp6uqqkqHDh2SJP3zn//U7t27NWvWLOPJfOOLL75QV1eXwsPDe6yPiIgIqKuUX3r//ffV1NTU47+nQ4YMUWpqqmpqagb8+N/Kb+09nzwejxYvXqwZM2Z8K34rrK/s379faWlp+uyzz3TJJZdoy5YtGj9+vPVYPrN582bt27fPr9+/PZvU1FQ9/fTTGjt2rD7++GOtWLFC1113nQ4cOKDIyEjr8b6xI0eOaN26dSooKNC9996rPXv26Fe/+pXCwsKUnZ1tPZ7Pbd26VSdPntTPf/5z61F8ZunSpWptbVViYqJCQkLU1dWlBx98UPPmzbMezSciIyOVlpamlStXaty4cXK73XruuedUU1OjK6+80no8n2tqapKk7t+m/iW329392EC64GMkNzdXBw4cCLjSHTt2rOrr69XS0qIXXnhB2dnZ2rVrV0AESWNjo/Lz81VZWXnG/7UEiv/7f5eTJk1SamqqRo4cqeeff16333674WS+4fF4lJKSolWrVkmSpkyZogMHDqi8vDwgY+TJJ5/UrFmzvvZr1P3J888/r2effVabNm3SNddco/r6ei1evFixsbEB83f4zDPPaMGCBYqLi1NISIimTp2quXPnqq6uznq0gHNBv02Tl5enl156Sa+++qquuOIK63F8KiwsTFdeeaWSk5NVUlKipKQkPfLII9Zj+URdXZ2OHTumqVOnKjQ0VKGhodq1a5ceffRRhYaGqqury3pEnxs6dKiuvvpqHT582HoUn4iJiTkjjMeNGxdQb0V96cMPP9Qrr7yihQsXWo/iU3fffbeWLl2qn/70p5o4caJuu+02LVmypPtLUgPBmDFjtGvXLp06dUqNjY2qra3V559/rtGjR1uP5nPR0dGSpObm5h7rm5ubux8bSBdkjDiOo7y8PG3ZskX/+Mc/NGrUKOuRBpzH41FHR4f1GD5x0003af/+/aqvr+9eUlJSNG/ePNXX1yskJMR6RJ87deqU3nvvPcXExFiP4hMzZsw44+P0hw4d0siRI40mGjhPPfWUoqKiNHv2bOtRfOr06dM9vhRVkkJCQuTxeIwmGjgXX3yxYmJi9Omnn2rnzp26+eabrUfyuVGjRik6OlpVVVXd61pbW/Xmm2+el/sNL8i3aXJzc7Vp0yb99a9/VWRkZPf7YUOGDFFERITxdN9cYWGhZs2apREjRqitrU2bNm1SdXW1du7caT2aT0RGRp5xf8/FF1+syy67LGDu+7nrrruUmZmpkSNH6qOPPlJxcbFCQkI0d+5c69F8YsmSJZo+fbpWrVqln/zkJ6qtrdX69eu1fv1669F8yuPx6KmnnlJ2drZCQwPrP7eZmZl68MEHNWLECF1zzTV66623VFpaqgULFliP5jM7d+6U4zgaO3asDh8+rLvvvluJiYnKycmxHq1fTp061ePq6vvvv6/6+npdeumlGjFihBYvXqwHHnhAV111lUaNGqXly5crNjZWc+bMGfjhBvzzOt9CknpdnnrqKevRfGLBggXOyJEjnbCwMOfyyy93brrpJufvf/+79VgDKtA+2puVleXExMQ4YWFhTlxcnJOVleUcPnzYeiyf+tvf/uZMmDDBcblcTmJiorN+/XrrkXxu586djiTn4MGD1qP4XGtrq5Ofn++MGDHCCQ8Pd0aPHu0sW7bM6ejosB7NZyoqKpzRo0c7YWFhTnR0tJObm+ucPHnSeqx+e/XVV3v9ty87O9txnP9+vHf58uWO2+12XC6Xc9NNN523n90gxwmgX5cHAAD8zgV5zwgAAPj2IEYAAIApYgQAAJgiRgAAgCliBAAAmCJGAACAKWIEAACYIkYAAIApYgQAAJgiRgAAgCliBAAAmCJGAACAqf8F6A/Du0Oj6+8AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}