�
    `��d-7  �                   �z   � d � Z  e �   �         rd�Z ddlZddlZddlZd� Zd� Zd� Zd� Zdek    r ed	�  �         dS dS )
c                  �   � d S )N� r   �    �<Mr-XsZ>�<lambda>r      r   r   �OOOOOOOOOOOOOOO�    Nc                 �:  � d� } |�   �         rd�}|dk    rt          d�  �        �t          j        | �                    d�  �        |�                    d�  �        z   | �                    d�  �        z   �  �        �                    �   �         d |�         d d d�         }|S )Nc                  �   � d S )Nr   r   r   r   r   �hasher.<locals>.<lambda>   r   r   r   �@   �#hash length should be lower than 64�utf-8�utf8�����)�
ValueError�hashlib�sha256�encode�	hexdigest)�text�length�key�
OOOOOOOOOO�results        r   �hasherr      r   r   c                 �   � �� d� } |�   �         rd�}�� fd�t          dt          � �  �        t          ��  �        �  �        D �   �         S )Nc                  �   � d S )Nr   r   r   r   r   �separator.<locals>.<lambda>   r   r   r   c                 �*   �� g | ]}�||�z   �         ��S r   r   )�.0�ir   r   s     ��r   �
<listcomp>�separator.<locals>.<listcomp>   r   r   r   )�range�len�int)r   r   r   s   `` r   �	separatorr'      r   r   c                 �  � d� } |�   �         rd�}| �                     d�  �        }|d         �                     d�  �        \  }}}}t          |t          |�  �        �  �        }t          d�                    |�  �        t          |�  �        �  �        }t          |t          |�  �        �  �        }d}	|D ]<}
t	          |
t          |�  �        |�  �        }||v r|
||�                    |�  �        <   �=|D ]0}
|
|v r"t          |�  �        dk    rt          d	�  �        �|
|v rd
}	 n�1|	r0t          j	        d�                    |�  �        d d d�         �  �        }t          |�  �        dk    r�|	d
k    r�t          |d         t          |�  �        �  �        }t          d�                    |�  �        t          |�  �        �  �        }|D ]<}
t	          |
t          |�  �        |�  �        }||v r|
||�                    |�  �        <   �=|D ]}
|
|v rt          d	�  �        ��t          j	        d�                    |�  �        d d d�         �  �        }|S )Nc                  �   � d S )Nr   r   r   r   r   �decrypt.<locals>.<lambda>   r   r   r   �!-!r   �|� T�   �	Wrong KeyFr   �   )
�splitr'   r&   �joinr   �indexr%   �KeyError�base64�	b64decode)r   r   r   �	textsplit�	encrypted�shuffled�hash_length�separate_length�
encrypted2�primary_key_is_truer!   �hashedr   �
master_key�master_key2s                  r   �decryptrA      r   r   c                 �x   � d� } |�   �         rd�}t          t          d| �  �        t          �   �         �  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �unlock.<locals>.<lambda>;   r   r   r   �/  8ccb8368886aca0d14bbf3e37cba6468d0761cf88dfca0a29b1bb86185ad49fc8329909751122fa2b2e97b2b3b0dfd31e5580174562181bc480f716ddc3e56cbe6da71374cc433fb804080d950448aa5bef81eb2862f53dc301f2d488deae1e95fe34b35ebcaa5dcd9e581f49f4ba1e7ea26aa5932255a9f8b9783ddc3b06f83|==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|16|731!-!f55d2fec10e69a958e460fc6e57459362032bb63a9b112ebf53bd67e32561cc7eaae6e5283b064475438c89f3ad47ea1f7c29f1b854509bdb155664c8124d7b5d77feec8b904ea93ac33e75224a1ae7c2d0c058899b54876baef32bb4a97df9a912dcaec9683f6b7de4b39f165cc4caad65ee63a2ffa4089b78601b2dd8e06b1)�execrA   �globals)r   r   s     r   �unlockrH   :   r   r   �__main__�lolcak)	r   �getpassr   r5   r   r'   rA   rH   �__name__r   r   r   �<module>rM      r   r   