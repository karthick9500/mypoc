import requests
import concurrent.futures
import time
import datetime


def get_urls():
    return [
    "https://api-dev-internal.edb.notprod.thenbs.io/referencedata/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/address/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/customers/match/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/referencedata/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/address/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/customers/match/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/referencedata/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/address/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/customers/match/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/referencedata/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/address/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/customers/match/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/involved-party-sanctions/v1/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/dpv/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/idgenerator/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health",
    "https://api-dev-internal.edb.notprod.thenbs.io/applicationstore/v2/health"
    ]

def load_url(url, timeout):

    headers = {'apikey': ''}
    test =  requests.get(url, timeout = timeout,headers=headers)
    return test
resp_err = 0
resp_ok = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=120) as executor:

    future_to_url = {executor.submit(load_url, url, 120): url for url in     get_urls()}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
            #print (st)
            data = future.result()
            print(str(data.status_code) +" --  "+ str(st))
        except Exception as exc:
            resp_err = resp_err + 1
        else:
            resp_ok = resp_ok + 1
