�
    ���f'  �                   �$   � d � Z d� Zd� Z e�        y)c                 �  � |j                  d�      d   j                  �       }|j                  | �      d   j                  �       }|� d|� �}t        d|�       t        dd�      5 }|j	                  |dz   �       d d d �       y # 1 sw Y   y xY w)N�:�   �   �Converted ==> z	combo.txt�a�
��split�strip�print�open�write)�	separated�content�email�password�output�Outputs         �Cloud.py�convertToMailPassr      s�   � ��M�M�#��q�!�'�'�)�E��}�}�Y�'��*�0�0�2�H��w�a��z�"�F�	�
�6�"�	�k�#�	� "�&����V�D�[�!�"� "� "�s   �$B�Bc                 ��   � |j                  | �      d   j                  �       }|� }t        d|�       t        dd�      5 }|j	                  |dz   �       d d d �       y # 1 sw Y   y xY w)Nr   r   z
emails.txtr   r   r	   )r   r   r   r   r   s        r   �convertToMailr      sa   � ��M�M�)�$�Q�'�-�-�/�E��w�F�	�
�5�!�	�l�3�	� "�6����V�D�[�!�"� "� "�s   �A�A%c                  �  � t        d�       t        d�       t        d�       t        d�       t        d�       t        d�       t        t        d�      �      } t        d�      }|d	k(  rd
}t        t        d�      ddd��      5 }|j	                  �       }d d d �       | d	k(  r5D ]/  }	 t        ||j                  dd�      j                  dd�      �       �1 y | dk(  r5D ]/  }	 t        ||j                  dd�      j                  dd�      �       �1 y y # 1 sw Y   �~xY w# t        $ r}t        dt        |�      �       Y d }~��d }~ww xY w# t        $ r
}Y d }~�yd }~ww xY w)NzCODED BY  @donussefz JOIN https://t.me/freespamtools2� z$CLOUD TOOL!!!Join VIP For more toolsuO   [+] 0 : Convert URL:EMAIL OR USERNAME :PASSWORD TO EMAIl OR USERNAME:PASSWORD zD[+] 1 : Convert URL:EMAIL OR USERNAME:PASSWORD TO EMAIl OR USERNAME z	Option : z Data separated with? Example(|) �    �|zList : �r�utf8�ignore)�encoding�errorszhttps://zhttp://zFailed r   )
r   �int�inputr   �	readlinesr   �replace�	Exception�strr   )�optionr   �RD�rd�ClOUDS�es         r   �mainr-      sC  � �	�
� �	�
,�-�	�"�I�	�
0�1�	�
[�\�	�
P�Q���{�#�$�F��8�9�I��A�~��	�	�e�I��s�F�(�	C� �r��\�\�^��� ��{��F��!�)�F�N�N�:�b�,I�,Q�,Q�R[�\^�,_�`� � 
�1���F���i����z�"�(E�(M�(M�i�XZ�([�\� � 
�� �� � ��i��A��'����� � ����s6   �D�%,D�,E�D�	E�$D>�>E�	E�EN)r   r   r-   � �    r   �<module>r0      s   ��"�"��< �r/   